import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

import re
import string
import os

import wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

from textblob import TextBlob

from PIL import Image, ImageDraw, ImageFont
import plotly.express as px

st.set_page_config(layout="wide")

st.title('Twitter Sentiment Analysis')
st.subheader('for improving SDG goals in hotel industry')

def clean_tweet(text):
    # remove user mentions
    text = re.sub(r'@[A-Za-z0-9]+', '', text)

    # remove hashtags
    text = re.sub(r'#', '', text)

    # remove retweets:
    text = re.sub(r'RT[\s]+', '', text)

    # remove urls
    text = re.sub(r'https?:\/\/\S+', '', text)

    # remove punctuations
    text = re.sub(r'[^\w\s]', '', text)

    # remove numbers
    text = re.sub(r'\d+', '', text)

    # remove stop words
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(text)

    filtered_text = [word for word in word_tokens if word not in stop_words]

    filtered_text = ' '.join(filtered_text)

    return filtered_text

# sentiment analysis
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
    return TextBlob(text).sentiment.polarity




def load_data():
    df1 = pd.read_csv('tweets/search_food quality_16_07_2023.csv')
    df2 = pd.read_csv('tweets/search_green hotel_16_07_2023.csv')
    df3 = pd.read_csv('tweets/search_hotel_16_07_2023.csv')
    df4 = pd.read_csv('tweets/search_motel_16_07_2023.csv')
    df5 = pd.read_csv('tweets/search_vacation_16_07_2023.csv')
    # join all the dataframes
    df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)  
    return df

with st.spinner('Loading Data...'):
    df = load_data()

with st.spinner('Cleaning Data...'):
    df['clean_tweet'] = df['tweet'].apply(clean_tweet)

st.subheader('Raw Twitter data')
st.dataframe(df)

df['Subjectivity'] = df['clean_tweet'].apply(getSubjectivity)
df['Polarity'] = df['clean_tweet'].apply(getPolarity)

df_negative = df[df['Polarity'] < 0]
df_positive = df[df['Polarity'] > 0]
df_neutral = df[df['Polarity'] == 0]

# sentiment bar chart
def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'
    
df['Analysis'] = df['Polarity'].apply(getAnalysis)

fig = px.bar(df, x='Analysis', y=df.index, color='Analysis', title='Sentiment Analysis')
st.plotly_chart(fig, use_container_width=True)

fig = px.pie(df, values=df.index, names='Analysis', title='Sentiment Analysis')
st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Word Cloud Analysis'):
    st.subheader('Negative Tweets Word Cloud')
    # word cloud only for negative tweets
    all_words = ' '.join([text for text in df_negative['clean_tweet']])
    wc = WordCloud(stopwords=STOPWORDS, width=1200, height=700, random_state=21, max_font_size=110).generate(all_words)

    fig, ax = plt.subplots(figsize=(12, 8))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)

    # word cloud only for positive tweets
    st.subheader('Positive Tweets Word Cloud')
    all_words = ' '.join([text for text in df_positive['clean_tweet']])
    wc = WordCloud(stopwords=STOPWORDS, width=1200, height=700, random_state=21, max_font_size=110).generate(all_words)

    fig, ax = plt.subplots(figsize=(12, 8))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)

    # word cloud only for neutral tweets
    st.subheader('Neutral Tweets Word Cloud')
    all_words = ' '.join([text for text in df_neutral['clean_tweet']])
    wc = WordCloud(stopwords=STOPWORDS, width=1200, height=700, random_state=21, max_font_size=110).generate(all_words)

    fig, ax = plt.subplots(figsize=(12, 8))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)





