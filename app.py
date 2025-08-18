import streamlit as st
from functions import plot_ts

st.title('Historico de cotações')
st.write('Veja os históricos de cotações das empresas')

ticker = st.sidebar.text_input(
    'Escolha o ticker:', value='AAPL'
)

fig = plot_ts.plot(ticker)

st.plotly_chart(fig)