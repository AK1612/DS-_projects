import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Singapore flat resale price prediction model")

add_selectbox=st.sidebar.selectbox("select option",("HOME","PRICE PREDICTION"))

if add_selectbox=="HOME":
   
   st.title("Singapore flat resale price prediction model")

if add_selectbox=="PRICE PREDICTION":

    quantity=st.number_input('enter quantity in tons', min_value=0, max_value=10000)
    
