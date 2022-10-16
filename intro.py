import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

from bokeh.plotting import figure

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

df1= df.iloc[0:10]
st.line_chart(data=df1, x = 'Ship Date', y = 'Profit', width=0, height=0, use_container_width=True)


st.bar_chart(data=df1, x = 'Ship Date', y = 'Profit')


# metrics
st.metric("Total Sales", 1000, 10)

st.metric("Total Profit", "$ 10M", "-2.3%")

st.title("Charting")

with st.sidebar:
    st.title("Dashboard store")
    freq = st.selectbox("Masukkan frekuensi", ('D', 'W', 'M', 'Q', 'Y'));


 
    
'''
# Daftar Pustaka

[BPS](https://www.bps.go.id/indicator/16/1150/1/jumlah-kunjungan-wisatawan-mancanegara-per-bulan-ke-indonesia-menurut-pintu-masuk-2017---sekarang.html)

[Kawal Covid 19](https://docs.google.com/spreadsheets/d/1ma1T9hWbec1pXlwZ89WakRk-OfVUQZsOCFl4FwZxzVw/htmlview)

[Model Decision Tree untuk Prediksi Jadwal Kerja menggunakan Scikit-Learn](https://jurnal.umj.ac.id/index.php/semnastek/article/view/5239/3517)


'''    
df2 = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df2)
