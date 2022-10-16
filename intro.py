import streamlit as st
import pandas as pd
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
from PIL import Image

#from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
#from bokeh.plotting import figure, show, output_notebook
#output_notebook()
st.set_page_config(layout="wide")

'''
    # Analisis Pemulihan sektor Pariwisata pasca Pandemi di Indonesia
    Capstone Project with **streamlit** by Zulfikri Syafnur
    
    ---
'''

'''
## Kesiapan Stakeholder dalam membangkitkan kembali Pariwisata

_________________

[Pariwisata](https://id.wikipedia.org/wiki/Pariwisata) merupakan cara suatu negara mempromosikan negara tersebut sehingga dapat dikinjungi oleh banyak orang. 
Di Indonesia, contoh pariwisata yang menjadi tujuan wisata yang terkenal di dunia adalah [Bali](https://bali.com/). 
Bali terkenal dengan berbagai objek wisatanya seperti wisata alam, wisata budaya, dan wisata bahari
'''

st.title("Dashboar Latihan")
st.write("Nama Saya Zul")
st.markdown("Nama Saya Zul")
st.markdown("---")


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
    freq = st.selectbox("Masukkan frekuensi", ('D', 'W', 'M', 'Q', 'Y'));
