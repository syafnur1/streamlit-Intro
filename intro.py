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

st.sidebar.write(
    '''
    # Simple Stock Price App
    Made with **streamlit** by riztekur
    '''
)


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
    freq = st.selectbox("Masukkan frekuensi", ('D', 'W', 'M', 'Q', 'Y'));
