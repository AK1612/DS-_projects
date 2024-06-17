import folium
import streamlit as st
from streamlit_folium import st_folium
import json
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

st.title("Geo Visualisation")

df=pd.read_json("E:\python\sample_airbnb.json")
cols=['listing_url','name','summary','space','description','neighborhood_overview','notes','transit','access','interaction','house_rules','last_scraped','calendar_last_scraped','images','host','reviews','reviews_per_month','weekly_price','monthly_price','security_deposit','cleaning_fee','first_review','last_review']
df=df.drop(columns=cols,axis=1)
g=df.isna().sum()
df['bedrooms']=df['bedrooms'].fillna(df['bedrooms'].mode())
df['beds']=df['beds'].fillna(df['beds'].mode())
df['bathrooms']=df['bathrooms'].fillna(df['bathrooms'].mode())
df=pd.concat([df.drop(['address'],axis=1),df['address'].apply(pd.Series)],axis=1)
df=pd.concat([df.drop(["location"],axis=1),df['location'].apply(pd.Series)],axis=1)
df=df.drop(['type'],axis=1)
#ARRANGE THE LATITUDE AND LONGITUDE TO PLOT IN FOLIUM MAP
for i in range(len(df['coordinates'])):
    df['coordinates'][i][0],df['coordinates'][i][1]=df['coordinates'][i][1],df['coordinates'][i][0]


# User input for filtering
name_filter = st.selectbox('Select country name to filter by:',options=df['country'].unique().tolist())
price_filter = st.slider('Select price range:', 0, 3000, (1000, 2000))
type_filter = st.selectbox('Select room type to filter by:', options=['All'] + df['room_type'].unique().tolist())


# Filter DataFrame based on user input
filtered_df = df[(df['country'].str.contains(name_filter, case=False)) &
                 (df['price'] >= price_filter[0]) & (df['price'] <= price_filter[1])]

if type_filter != 'All':
    filtered_df = filtered_df[filtered_df['room_type'] == type_filter]


# Display the filtered DataFrame
st.write(filtered_df)

# Convert the lists of coordinates to Shapely Point objects
filtered_df['geometry'] = filtered_df['coordinates'].apply(lambda coords: Point(coords[1], coords[0]))

# Convert the DataFrame to a GeoDataFrame
gdf = gpd.GeoDataFrame(filtered_df, geometry='geometry', crs="EPSG:4326")


m = folium.Map(zoom_start=13)

folium.GeoJson(gdf,
                zoom_on_click=True,
                tooltip=folium.GeoJsonTooltip(fields=["country", "price", "beds"]),
                popup=folium.GeoJsonPopup(fields=["country", "price", "beds"])).add_to(m)

st_folium(m, width=700, height=500)

