# pip install streamlit streamlit-option-menu

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
st.sidebar.header()

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

