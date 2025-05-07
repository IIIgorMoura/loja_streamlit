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

# filtros de gráfico (flex view)
st.sidebar.header()