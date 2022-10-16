import streamlit as st
import pandas as pd
import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
from PIL import Image
import lorem

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
[Pariwisata](https://id.wikipedia.org/wiki/Pariwisata) merupakan cara suatu negara mempromosikan negara tersebut sehingga dapat dikinjungi oleh banyak orang. 
Di Indonesia, contoh pariwisata yang menjadi tujuan wisata yang terkenal di dunia adalah [Bali](https://bali.com/). 
Bali terkenal dengan berbagai objek wisatanya seperti wisata alam, wisata budaya, dan wisata bahari
'''

st.title("Dashboar Latihan")
st.write("Nama Saya Zul")
st.markdown("Nama Saya Zul")
st.markdown("---")

# Image
image = Image.open("TurisTahun.png")
st.image(image, use_column_width='auto', caption = "Sumber : Badan Pusat Statistik")

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

    
#Penggunaan Kolom
st.title("Kolom")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(lorem.paragraph())

with col2:
    st.write(lorem.paragraph())

with col3:
    st.write(lorem.paragraph())    
    
'''
# Daftar Pustaka

[BPS](https://www.bps.go.id/indicator/16/1150/1/jumlah-kunjungan-wisatawan-mancanegara-per-bulan-ke-indonesia-menurut-pintu-masuk-2017---sekarang.html)

[Kawal Covid 19](https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/htmlview)

[Model Decision Tree untuk Prediksi Jadwal Kerja menggunakan Scikit-Learn](https://jurnal.umj.ac.id/index.php/semnastek/article/view/5239/3517)


'''    
