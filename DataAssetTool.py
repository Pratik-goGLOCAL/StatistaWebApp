# Import Packages
import pandas as pd
import streamlit as st
import numpy as np
import os
import pickle
import subprocess
import json
from urllib.parse import urljoin
import re
from loguru import  logger

st.set_page_config(
    page_title="DataAssetTool"
)

st.title("Data Asset Tool")

# st.write('The Data Asset Tool contains the web scraped E-Commerce Statistical Data from SimilarWeb, Statista, etc. websites')

country_names = os.listdir('statista_data')
hsn_codes_level1 = pd.read_csv('mappings/hsn_codes_level1.csv')
# with open('mappings/hsn_code_level1.pickle', 'rb') as handle:
#     hsn_codes_level1 = pickle.load(handle)

with open('mappings/hsn_codes_level2.pickle', 'rb') as handle:
    hsn_codes_level2 = pickle.load(handle)


# Initialize Variables
if "get" not in st.session_state:
    st.session_state["get"] = ""
if "country" not in st.session_state:
    st.session_state["country"] = ""
if "category_name_1" not in st.session_state:
    st.session_state["category_name_1"] = ""
if "hsn_code_1" not in st.session_state:
    st.session_state["hsn_code_1"] = ""
if "category_name_2" not in st.session_state:
    st.session_state["category_name_2"] = ""
if "hsn_code_2" not in st.session_state:
    st.session_state["hsn_code_2"] = ""

# Select the Country
country = st.selectbox(label='Select Country',
                    options=[x.title() for x in country_names])
st.session_state['country'] = country.lower()

# Select the hsn level 1 Category
hsn_category = st.selectbox(label='Select Category Name/HSN code',
                    options=hsn_codes_level1)
# st.write('The options selected are:', region)
st.session_state['hsn_code_1'] = hsn_category.split('  ')[0]
st.session_state['category_name_1'] = hsn_category.split('  ')[1]

hsn_code2 = hsn_codes_level2[st.session_state['hsn_code_1']]
hsn_code2.append('ALL')
default_ix = hsn_code2.index('ALL')
# Select the hsn_level 2 Category
hsn2_category = st.selectbox(label='Select Sub-category Name/HSN code',
                    options=hsn_code2,
                    index=default_ix)
st.session_state['hsn_code_2'] = hsn2_category
# st.session_state['hsn_code_2'] = hsn_category.split('  ')[0]
# st.session_state['category_name_2'] = hsn_category.split('  ')[1]

get = st.button("Get")
st.session_state['get'] = get