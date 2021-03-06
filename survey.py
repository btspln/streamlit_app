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
data = pd.read_csv('https://raw.githubusercontent.com/btspln/streamlit_app/1afe6940de6ca9b057907847818e235ae8ee3148/beispiel_comments.csv')

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(255, 127, 127);
}
</style>""", unsafe_allow_html = True)

length = data.shape[0]
nr = random.randint(0, length - 1)

st.subheader('Please rate the following comment: \n')
st.text(' ')
st.markdown("""---""")
st.markdown(data['comment'][nr])
st.markdown("""---""")
st.text(' ')
st.text(data['id'][nr])
st.text(' ')

pos_button = st.button('POSITIVE')
neu_button = st.button('NEUTRAL')
neg_button = st.button('NEGATIVE')

st.text(' ')
st.text(' ')

if pos_button:
    bew = 'POSITIVE'
elif neu_button:
    bew = 'NEUTRAL'
else:
    bew = 'NEGATIVE'

@st.cache(allow_output_mutation = True)
def get_data():
    return []

get_data().append({"Comment ID": str(data['id'][nr]), "Rating": bew})

df = pd.DataFrame(get_data())
df['Comment ID'] = df['Comment ID'].shift(1)
#df['Bewertung'][0] = None
st.dataframe(df[::-1][:-1])

st.text(' ')
st.text(' ')

csv = df.to_csv(index = False)
b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as  &lt;some_name&gt;.csv)'
st.markdown(href, unsafe_allow_html = True)
