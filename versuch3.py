# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 08:12:46 2021

@author: Balint.Psenak
"""

# RUN WITH:    streamlit run 'C:\Users\Balint.Psenak\OneDrive - insidemedia.net\Desktop\survey\versuch3.py'

import streamlit as st
import pandas as pd
import base64
from io import BytesIO

import random

#data = pd.read_csv('https://github.com/btspln/streamlit_app/blob/main/beispiel_comments.csv')
#data = pd.read_csv('X:/alle/DataSolutions/Balint/beispiel_comments.csv')
data = pd.read_csv('https://raw.githubusercontent.com/btspln/streamlit_app/1afe6940de6ca9b057907847818e235ae8ee3148/beispiel_comments.csv', nrows = 8000)

st.subheader('Here is the text: \n')

nr = random.randint(5, 7500)
st.text(data['id'][nr])
st.markdown(data['comment'][nr])

#bew = st.selectbox('Bewertung:', ('', 'Positive', 'Negative'))

pos_button = st.button('POSITIVE')
neg_button = st.button('NEGATIVE')

if pos_button:
    bew = 'POSITIVE'
else:
    bew = 'NEGATIVE'

@st.cache(allow_output_mutation = True)
def get_data():
    return []

get_data().append({"comm_id": str(data['id'][nr]), "Bewertung": bew})

df = pd.DataFrame(get_data())
df['comm_id'] = df.comm_id.shift(1)
#df['Bewertung'][0] = None
st.dataframe(df[::-1])
