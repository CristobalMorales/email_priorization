import streamlit as st
import pandas as pd

st.title("Resumen diario de correos priorizados")

st.markdown("Esta app mostrará el resumen diario")

df_priority = pd.read_csv("data.csv")

st.table(data=df_priority)