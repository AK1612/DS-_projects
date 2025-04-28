import folium
import streamlit as st
from streamlit_folium import st_folium
import json
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import ast
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("D:/ds/airbnb/airbnb.csv")


def create_map():
    # Filter DataFrame based on user input
    filtered_df = df[(df['country'].str.contains(name_filter, case=False)) &
                     (df['price'] >= price_filter[0]) & (df['price'] <= price_filter[1])]

    if type_filter != 'All':
        filtered_df = filtered_df[filtered_df['room_type'] == type_filter]
    
    
    
    # Convert the lists of coordinates to Shapely Point objects

    filtered_df['coordinates'] = filtered_df['coordinates'].apply(ast.literal_eval)
    filtered_df['geometry'] = filtered_df['coordinates'].apply(lambda coords: Point(coords[1],coords[0]))
    st.session_state.filtered_df = filtered_df
    # Convert the DataFrame to a GeoDataFrame
    gdf = gpd.GeoDataFrame(filtered_df, geometry='geometry', crs="EPSG:4326")
    m = folium.Map(zoom_start=13)
    folium.GeoJson(gdf,
                    zoom_on_click=True,
                    tooltip=folium.GeoJsonTooltip(fields=["country", "price", "beds"]),
                    popup=folium.GeoJsonPopup(fields=["country", "price", "beds"])).add_to(m)
    return m,filtered_df

add_selectbox=st.sidebar.selectbox("select options",("HOME","GEO VISUALISATION","PRICE VARIATION ANALYSIS","OCCUPANCY RATE"))

if add_selectbox=="HOME":

    st.title("Airbnb User Friendly Data Visualisation")
    
if add_selectbox=="GEO VISUALISATION":
    st.title("Geo Visualisation")

    left_col, right_col = st.columns([1, 2]) 

    with left_col:  
     name_filter = st.selectbox('Select country:',options= df['country'].unique().tolist())
     price_filter = st.slider('Select price range:', 0, df['price'].max(),(0, df['price'].max()))
     type_filter = st.selectbox('Select room type:', options=['All'] + df['room_type'].unique().tolist())

    with right_col:
        map,data = create_map()
        st_folium(map, width=600, height=300)
        
    st.dataframe(data)

if add_selectbox=="PRICE VARIATION ANALYSIS":


    country_filter=st.selectbox('select country',options=['All'] + df['country'].unique().tolist())

    if country_filter=='All':
        if st.button('Get'):
          # Aggregate data
          agg_data = df.groupby(['country', 'room_type']).agg({'price': 'mean'}).reset_index()
          # Plotly bar plot
          st.subheader('Average Price variation by Country and Room Type')
          fig = px.bar(agg_data, x='country', y='price', color='room_type', barmode='group',
                       labels={'price': 'Average Price', 'country': 'Country', 'room_type': 'Room Type'},
                       title='Average Price by Country and Room Type')
          st.plotly_chart(fig)
    else:
        if st.button('Get'):
            filtered_df = df[(df['country'].str.contains(country_filter, case=False))]
            st.subheader('Average Price variation by Room Type')
            fig = px.bar(filtered_df, x='country', y='price', color='room_type', barmode='group',
                        labels={'price': 'Average Price', 'country': 'Country', 'room_type': 'Room Type'},
                        title='Average Price by Country and Room Type')
            st.plotly_chart(fig)

if add_selectbox=="OCCUPANCY RATE":


    df1=pd.read_csv("D:/ds/airbnb/airbnb1.csv")
    df1['id']=df1['id'].astype('str')
    lef_col,rig_col=st.columns([1,3])
    with lef_col:
        country_filter=st.selectbox('select country',options=['All']+df1['country'].unique().tolist())
        if country_filter != 'All':
            filtered_df1=df1[(df1['country'].str.contains(country_filter, case=False))]
            id_filter=st.selectbox('select id',options= filtered_df1['id'].unique().tolist())
        else:
            st.text('PLEASE SELECT A COUNTRY')    

    if st.button('Get'):
                filtered_dft = filtered_df1[(filtered_df1['id'].str.contains(id_filter, case=False))]
                fig=px.line(filtered_dft,x='date',y='count',title='Occupancy Rate of ' + 'Id: '+ id_filter +' in '+ country_filter +' Over The Years')
                with rig_col:
                    st.plotly_chart(fig)
                
                st.dataframe(filtered_dft)

                    
                
                