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
import fuzzywuzzy as fuzz

st.set_page_config(
    page_title="DataAssetTool"
)
st.title("ECommerceDB Data Store")

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
try:
    if st.session_state['get']:
        # st.write('The Data File corresponding to the HSN code {} belonging to the category {}'.format(st.session_state['hsn_code_1'].zfill(4),st.session_state['category_name_1']))
        # path = 'dgci_data/'+st.session_state['hsn_code_1'].zfill(4)+'.csv'
        path = 'ecommercedb_data/'+st.session_state['country'].title()
        try:
            filename1 = [x for x in os.listdir(path) if st.session_state['hsn_code_1'] in x][0]
            logger.info('filename 1 is {}'.format(filename1))
            files = os.listdir(path+ '/'+filename1)
            logger.info('files are {}'.format(files))
            file_vals = []
            logger.info('fuzzy matching with {}'.format(st.session_state['category_name_2']))
            for file in files:
                file_vals.append(fuzz.ratio(st.session_state['category_name_2'],file))
            logger.info('fuzzy matching with {}'.format(file_vals))
            filename2 = files[np.argmax(file_vals)]
            logger.info('filename 2 is {}'.format(filename2))
            path = path+'/'+filename1+'/'+filename2
            req_file = os.listdir(path)[0]
            logger.info('required file path is {}'.format(path+'/'+req_file))
            df = pd.read_excel(path+'/'+req_file)
            df.fillna('NULL',inplace = True)
        except:
            path = 'ecommercedb_data/'+st.session_state['country'].title()+'/All-categories/--'
            filename = os.listdir(path)[0]
            df = pd.read_excel(path+'/'+filename)
        st.dataframe(df)
        csv = convert_df(df)
        st.download_button(
            label="Download",
            data=csv,
            file_name='DataStore/'+'res.csv',
            mime='text/csv',
        )
except:
    st.write('Please select the desired categories on the Data Assets Tool page')