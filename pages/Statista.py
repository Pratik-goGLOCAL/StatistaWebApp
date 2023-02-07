# Import Packages
import pandas as pd
import streamlit as st
import numpy as np
import os
import pickle as pkl
import subprocess
import json
from urllib.parse import urljoin
import re
import sys
from loguru import  logger

st.set_page_config(
    page_title="DataAssetTool"
)

st.title("Statista Data Store")

country_names = os.listdir('statista_data')

# Initialize Variables
if "category_name" not in st.session_state:
    st.session_state["category_name"] = ""
if "country" not in st.session_state:
    st.session_state["country"] = ""
if "insights" not in st.session_state:
    st.session_state["insights"] = ""
if "hsn_code" not in st.session_state:
    st.session_state["hsn_code"] = ""

# Select the Country
country = st.selectbox(label='Select Country',
                    options=[x.title() for x in country_names])
st.session_state['country'] = country.lower()

categories = os.listdir('statista_data/'+country.lower())

# Select the Category
category = st.selectbox(label='Select Category',
                    options=[x.replace('-',' ').title() for x in categories])
# st.write('The options selected are:', region)
st.session_state['category_name'] = category.replace(' ','-').lower()

insights = os.listdir('statista_data/'+st.session_state['country']+'/'+st.session_state['category_name'])
display = {x.split('.')[0].title():x for x in insights}
# Select the Insights
insight = st.selectbox(label='Select Insights Desired',
                    options=list(display.keys()))
# st.write('The options selected are:', region)
st.session_state['insights'] = display[insight]


@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

get = st.button("Get")


if get:
    path = 'statista_data/'+st.session_state['country']+'/'+st.session_state['category_name']+'/'+ st.session_state['insights']
    df = pd.read_excel(path)
    st.dataframe(df)
    csv = convert_df(df)
    st.download_button(
        label="Download",
        data=csv,
        file_name='DataStore/'+'res.csv',
        mime='text/csv',
    )