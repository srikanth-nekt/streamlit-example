import streamlit as st
import pandas as pd
# import pyxlsb

df = pd.read_csv("GG_17.csv")
# df = pd.read_excel("GG_17.xlsb")

# st.table(df)
st.write(df)