import streamlit as st
import pandas as pd

df = pd.read_csv('store - store.csv')

st.set_page_config(layout="wide")

st.title("Dashboar Latihan")

st.write("Nama Saya Zul")

st.header("Ini header")

st.dataframe(df)

st.caption('Ini caption')


st.line_chart(['Quantity'])








