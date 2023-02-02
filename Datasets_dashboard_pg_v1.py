# Import Packages
import pandas as pd
import plotly.express as px
import streamlit as st
import xlrd

data = pd.read_excel(io= 'Statista-Market-Insights-Albania---Revenue-Furniture (1).xlsx',
                    engine= 'openpyxl',
)