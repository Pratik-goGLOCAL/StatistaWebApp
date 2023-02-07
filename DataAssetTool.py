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

st.title("Data Asset Tool")

st.write('The Data Asset Tool contains the web scraped E-Commerce Statistical Data from SimilarWeb, Statista, etc. websites')