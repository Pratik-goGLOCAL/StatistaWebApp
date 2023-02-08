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
st.title("SimilarWeb Data Store")

if st.session_state['get']:
    path = 'SimilarWeb/'+st.session_state['country']+'/'+st.session_state['category_name']+'/'+ st.session_state['insights']
    df = pd.read_excel(path)
    st.dataframe(df)
    csv = convert_df(df)
    st.download_button(
        label="Download",
        data=csv,
        file_name='DataStore/'+'res.csv',
        mime='text/csv',
    )