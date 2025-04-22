import streamlit as st
import pandas as pd
from modelo_ia.modelo import prever_proximo

st.title("MVP IA - Roleta Online")
st.write("Visualização dos últimos números e previsão do próximo.")

df = pd.read_csv("dados/resultados.csv")
st.dataframe(df.tail(10))

if len(df) >= 3:
    entrada = df['numero'].tail(3).tolist()
    previsao = prever_proximo(entrada)
    st.success(f"Próximo número previsto: {previsao}")
else:
    st.warning("Insira ao menos 3 resultados para previsão.")