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


@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
filename = os.listdir('statista_data/'+st.session_state['country'])
path = 'statista_data/'+st.session_state['country']+'/'+filename
df = pd.read_csv(path)
if st.session_state['get']:
    st.dataframe(df)
    csv = convert_df(df)
    st.download_button(
        label="Download",
        data=csv,
        file_name='DataStore/'+'res.csv',
        mime='text/csv',
    )