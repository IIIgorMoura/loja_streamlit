# pip install streamlit streamlit-option-menu
# comando execução: python -m streamlit run projeto.py

import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

# dash vendas de produtos de diversas lojas

# configs iniciais
    # flaticon ou icon ou emoji
st.set_page_config(page_title='Dashboard - Vendas', page_icon='🛒', layout='wide')

# carregar dados
df = pd.read_excel('Vendas.xlsx')

# sidebar
st.sidebar.header('Selecione os Filtros')

# filtros de gráfico (flex view)
lojas = st.sidebar.multiselect(
    # titulo do filtro
    'Lojas',
    options=df['ID Loja'].unique(), #.unique() agrupa duplicidades
    default=df['ID Loja'].unique(), # opção pre selecionar (nesse caso, selecionar todos de começo)
    key='loja' # chave única (é como o nome de uma variavel)(quando for chamar novamente)
)

# filtro de produtos
produtos = st.sidebar.multiselect(
    'Produtos',
    options=df['Produto'].unique(),
    default=df['Produto'].unique(),
    key='produtos'
)

# filter dataframe de acordo com as opções selecionadas
    # o @nome é a key do filtro
    # `ID Loja` tem `` pois são 2 palavras mas são da mesma info
df_selecao = df.query('`ID Loja` in @lojas and Produto in @produtos')

# modelo que permite navegar entre 2 páginas

# tela principal
def Home():
    st.title('Faturamento das Lojas')

    # graficos e função da página
    total_vendas = df['Quantidade'].sum()
    media = df['Quantidade'].mean()
    mediana = df['Quantidade'].median()

    # trabalhar com colunas ou paginações usa st.columns
    total1,total2,total3 = st.columns(3) # o numero deve ser == a quant de variaveis

    # na coluna.. vai ter..
    with total1:
        # .metric = indicadores rápidos
            # principais infos visíveis de forma rápida
            # aqueles indicadores tipo cards de info, total de venda = 400.000
            # cards rápidos
        st.metric('Total Vendido', value=int(total_vendas)) # da para colocar icones
        
    with total2:
        st.metric('Média por Produto', value=f'{media:.1f}') # 1 num dps da ,

    with total3:
        st.metric('Mediana', value=int(mediana))

    st.markdown('---') # traçado para dar respiro visual na página

# mesmo padrão do matplotlib
def Graficos():
    # graph Bar, qnt prods/loja
    fig_barras = px.bar(
        df_selecao, 
        x='Produto', 
        y='Quantidade', 
        color='ID Loja', # cada loja vai ter uma cor diferente
        barmode='group', # diferenciar lojas por cor (agrupando, msm loja, msm cor)
        title='Quantidade de Produtos Vendidos por Loja'
    )

    # graph linha com total de vendas por loja
    fig_linha = px.line(
        df_selecao.groupby(['ID Loja']).sum(numeric_only=True).reset_index(),
        x='ID Loja',
        y='Quantidade',
        title='Total de Vendas por Loja'
    )

    # graphs lado a lado usa: .columns tmb
    graf1,graf2 = st.columns(2)
    with graf1:
        st.plotly_chart(fig_barras, use_container_width=True)
    with graf2:
        st.plotly_chart(fig_linha, use_container_width=True)

# se for usar varias telas
def sidebar():
    with st.sidebar:
        selecionado = option_menu(
            menu_title='Menu',
            options=['Home', 'Gráficos'],
            icons=['house','bar-chart'], # icons/emojis padrão
            default_index=0
        )

    if selecionado == 'Home':
        Home()
        Graficos()
    elif selecionado == 'Graficos':
        Graficos()

sidebar()