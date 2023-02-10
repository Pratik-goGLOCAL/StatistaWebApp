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

st.title("Miscalleneous Data Online")

files = []
for file in os.listdir('jp_morgan_data'):
    files.append(file)

with open("jp_morgan_data/"+files[0], "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.write(files[0].split('.')[0])
st.download_button(label='Download',
                    data=PDFbyte,
                    file_name='DataStore'+files[0],
                    mime='application/octet-stream')

with open("jp_morgan_data/"+files[1], "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.write(files[1].split('.')[0])
st.download_button(label='Download',
                    data=PDFbyte,
                    file_name='DataStore'+files[1],
                    mime='application/octet-stream')

with open("jp_morgan_data/"+files[2], "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.write(files[0].split('.')[0])
st.download_button(label='Download',
                    data=PDFbyte,
                    file_name='DataStore'+files[2],
                    mime='application/octet-stream')

with open("jp_morgan_data/"+files[3], "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.write(files[0].split('.')[0])
st.download_button(label='Download',
                    data=PDFbyte,
                    file_name='DataStore'+files[3],
                    mime='application/octet-stream')
                
with open("jp_morgan_data/"+files[4], "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.write(files[0].split('.')[0])
st.download_button(label='Download',
                    data=PDFbyte,
                    file_name='DataStore'+files[4],
                    mime='application/octet-stream')

with open("jp_morgan_data/"+files[5], "rb") as pdf_file:
    PDFbyte = pdf_file.read()
st.write(files[0].split('.')[0])
st.download_button(label='Download',
                    data=PDFbyte,
                    file_name='DataStore'+files[5],
                    mime='application/octet-stream')
