import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

#loading the  data
@st.cache_data
def load_data():
    path = 'data/kc_house_data.csv'
    df  = pd.read_csv(path)
    return df

#call the load data function
with st.spinner('Loading data...'):
    df = load_data()

#create title for ur app
st.title('House prce Data analytics')

#Display the dataset
if st.checkbox('show Dtataset', True):
     st.subheader('Dataset') 
     st.dataframe(df)   