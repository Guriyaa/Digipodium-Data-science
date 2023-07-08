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
st.title('House price Data analytics')
st.subheader('Key Performance indicator')

#to get the coloumns
cols = df.columns.tolist()
selected_cols = st.multiselect('select Columns',cols)
st.write(f'you selected:{len(selected_cols)} columns')

for col in selected_cols:
    st.subheader(f'Column: {col}')
    try:
        st.metric(label=f'Mean{col}',
                  value=round(df[col].mean()),
                  delta=round(df[col].std()))
        st.bar_chart(df[col], use_container_width=True)
    except:
        st.error(f'Cannot display {col} numeric data')