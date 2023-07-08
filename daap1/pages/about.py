import streamlit as st

# create a title for your app
st.title('House Price Data analysis')
st.subheader('About this app')
  
st.markdown("""
           This app performs simple dtat analysis on the **House price** dataset.
            *** python libraraies:**
            -pandas
            - streamlit
            -numpy
            -matplotlib
            -seaborn

            ** Data source:**[Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction)
           <img src=" https://www.oniriapictures.com/wallpapers/wp-content/uploads/21562-93ce0767da6c555cda717f253e22d85a.jpg">

             """, unsafe_allow_html=True)