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
st.title("DGCI Data Store")

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
try:
    if st.session_state['get']:
        descp = pd.read_csv('mappings/hsn_descp.csv')
        req_descp =  descp[descp['HSN']==int(st.session_state['hsn_code_1'].zfill(4))]['DESCP'].tolist()[0]
        st.write('The Data File corresponding to the HSN code {} belonging to the category {} displays the exports value in million US($)'.format(st.session_state['hsn_code_1'].zfill(4),st.session_state['category_name_1']))
        st.write('Description: {}'.format(req_descp))
        path = 'dgci_data/'+st.session_state['hsn_code_1'].zfill(4)+'.csv'
        df = pd.read_csv(path)
        df.fillna('NULL',inplace = True)
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
