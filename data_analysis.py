# agr hamien apna data ui pe show krna to pandas hamien bht se methods provide krta hai
# pandas is a python library used for data manipulation and analysis


import streamlit as st # web interface
import pandas as pd # For data manupilation
import datetime # datetime
import csv # For reading and writting CSV files
import os  # operating syystem for doing system level things



# creating a sidebar

st.sidebar.title('Data Analysis')
st.sidebar.header('Select an Option')

# data upload

uploaded_file = st.sidebar.file_uploader('Upload CSV file', type=['csv'])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
    st.header('Data Information')
    st.write(data.info())

    st.header('Data Summary')
    st.write(data.describe())






