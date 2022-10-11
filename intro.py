import streamlit as st
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(layout="wide")

st.write("Nama Saya Zul")
st.markdown("Nama saya **Rizki**")
st.markdown("---")

st.title("Dashboar Latihan")
st.header("Ini header")

st.code("import streamlit as st")

# Deklarasi dataset
df = pd.read_csv('store - store.csv')

# Data prep

# End of Data Prep
st.dataframe(df)

# metrics
st.metric("Total Sales", 1000, 10)

st.metric("Total Profit", "$ 10M", "-2.3%")

st.title("Charting")

with st.sidebar:
    st.title("Dashboard store")
    freq = st.selectbox("Masukkan frekuensi", ('D', 'W', 'M', 'Q', 'Y'))
    with st.expander("Ketahui lebih lanjut...");
