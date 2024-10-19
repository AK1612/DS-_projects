import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Singapore flat resale price prediction model")

add_selectbox=st.sidebar.selectbox("select option",("HOME","PRICE PREDICTION"))

if add_selectbox=="HOME":
   
   st.title("Singapore flat resale price prediction model")

if add_selectbox=="PRICE PREDICTION":

    town=st.selectbox('select town', ('ANG MO KIO' 'BEDOK' 'BISHAN' 'BUKIT BATOK' 'BUKIT MERAH' 'BUKIT TIMAH'
                        'CENTRAL AREA' 'CHOA CHU KANG' 'CLEMENTI' 'GEYLANG' 'HOUGANG'
                        'JURONG EAST' 'JURONG WEST' 'KALLANG/WHAMPOA' 'MARINE PARADE'
                        'QUEENSTOWN' 'SENGKANG' 'SERANGOON' 'TAMPINES' 'TOA PAYOH' 'WOODLANDS'
                        'YISHUN' 'LIM CHU KANG' 'SEMBAWANG' 'BUKIT PANJANG' 'PASIR RIS' 'PUNGGOL'))
    flat_type=st.selectbox('select flat type',('1 ROOM' '3 ROOM' '4 ROOM' '5 ROOM' '2 ROOM' 'EXECUTIVE'
                           'MULTI GENERATION' 'MULTI-GENERATION'))
    storey_range=st.selectbox('select storey range',('10 TO 12' '04 TO 06' '07 TO 09' '01 TO 03' '13 TO 15' '19 TO 21'
                               '16 TO 18' '25 TO 27' '22 TO 24' '28 TO 30' '31 TO 33' '40 TO 42'
                               '37 TO 39' '34 TO 36' '06 TO 10' '01 TO 05' '11 TO 15' '16 TO 20'
                               '21 TO 25' '26 TO 30' '36 TO 40' '31 TO 35' '49 TO 51' '46 TO 48'
                               '43 TO 45'))
    floor_area=st.slider('select floor area in sqm',min_value=33,max_value=400)
    flat_model=st.selectbox('select flat model',('IMPROVED' 'NEW GENERATION' 'MODEL A' 'STANDARD' 'SIMPLIFIED'
                            'MODEL A-MAISONETTE' 'APARTMENT' 'MAISONETTE' 'TERRACE' '2-ROOM'
                            'IMPROVED-MAISONETTE' 'MULTI GENERATION' 'PREMIUM APARTMENT' 'Improved'
                            'New Generation' 'Model A' 'Standard' 'Apartment' 'Simplified'
                            'Model A-Maisonette' 'Maisonette' 'Multi Generation' 'Adjoined flat'
                            'Premium Apartment' 'Terrace' 'Improved-Maisonette' 'Premium Maisonette'
                            '2-room' 'Model A2' 'DBSS' 'Type S1' 'Type S2' 'Premium Apartment Loft'
                            '3Gen'))
    lease_commence_year=st.slider('select lease commence year',min_value=1977,max_value=2020)


    with open("D:/ds/singapore flat resale  value prediction/regression_model1.pkl", "rb") as file:
           model = pickle.load(file)
              
    model_columns = pickle.load(open('D:/ds/singapore flat resale  value prediction/Rmodel_columns.pkl', 'rb'))
    
    
    new_data = {'month':2024, 'town':town, 'flat_type':flat_type, 'storey_range':storey_range, 'floor_area':floor_area,
                    'flat_model':flat_model, 'lease_commence_date':lease_commence_year}
    new_df = pd.DataFrame(new_data,[0])
    
        # One-hot encode the new data
    X_new = pd.get_dummies(new_df)
        
        # Align the new data with the columns from training
    X_new = X_new.reindex(columns=model_columns, fill_value=0)
        
        # Make prediction
    predict = model.predict(X_new)
    st.write(f"Price:{predict} ")
