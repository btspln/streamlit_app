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
data = pd.read_csv('https://github.com/btspln/streamlit_app/blob/main/beispiel_comments.csv')

st.subheader('Here is the text: \n')

nr = random.randint(5, 3000)
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

def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine = 'xlsxwriter')
    df.to_excel(writer, sheet_name = 'Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="extract.xlsx">Download xlsx file</a>' # decode b'abc' => abc

get_data().append({"comm_id": str(data['id'][nr]), "Bewertung": bew})

df = pd.DataFrame(get_data())
df['comm_id'] = df.comm_id.shift(1)
df['Bewertung'][0] = None
st.dataframe(df[::-1][:-1])

st.markdown(get_table_download_link(df), unsafe_allow_html = True)
