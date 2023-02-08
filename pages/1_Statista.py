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
try:
    if st.session_state['get']:
        filename = os.listdir('statista_data_csv/'+st.session_state['country'])

        path = 'statista_data_csv/'+st.session_state['country']+'/'+filename[0]
        df = pd.read_csv(path)
        df = df[df['Market_HSN']==int(st.session_state['hsn_code_1'])].copy()
        if st.session_state['hsn_code_2']!='ALL':
            df = df[df['Name']==st.session_state['hsn_code_2']].copy()
        insights = list(set(df['Chart'].tolist()))
        insights.append('ALL')
        default_ix = insights.index('ALL')
        # Select the insight
        insight = st.selectbox(label='Select Insights',
                            options=insights,
                            index = default_ix)
        df = df[df['Chart']==insight] if insight!='ALL' else df
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