import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# CREATE DATAFRAME OUT OF JSON FOR BETTER UDERSTANDING PROCESSING

df=pd.read_json("E:\python\sample_airbnb.json")

#REMOVE UNWANTED COLUMNS FROM DATAFRAME USING DROP COMMAND

cols=['listing_url','name','summary','space','description','neighborhood_overview','notes','transit','access','interaction','house_rules','last_scraped','calendar_last_scraped','images','host','reviews','reviews_per_month','weekly_price','monthly_price','security_deposit','cleaning_fee','first_review','last_review']
df=df.drop(columns=cols,axis=1)

#FIND EMPTY CELL USING ISNA COMMENT

g=df.isna().sum()

#FILL EMPTY CELL WITH MODE VALUE FOR CATEGORICAL COLUMN

df['bedrooms']=df['bedrooms'].fillna(df['bedrooms'].mode())
df['beds']=df['beds'].fillna(df['beds'].mode())
df['bathrooms']=df['bathrooms'].fillna(df['bathrooms'].mode())

#SPLIT ADDRESS COLUMN TO GET LONGITUDE AND LATITUDE 

df=pd.concat([df.drop(['address'],axis=1),df['address'].apply(pd.Series)],axis=1)
df=pd.concat([df.drop(["location"],axis=1),df['location'].apply(pd.Series)],axis=1)
df=df.drop(['type'],axis=1)

#USE Z SCORE TO REMOVE OUTLIERS
df['price_z']=round((df['price']-df['price'].mean())/df['price'].std(),2)
df=df[(df['price_z']<=3) & (df['price_z']>=-3)]


st.subheader('Box Plot of Prices')
fig = px.box(df, y='price', points='all',
             labels={'price': 'Price'},
             title='Box Plot of Prices')
st.plotly_chart(fig)

# Plot: Distribution of price_z
st.write('### Distribution of Price Z-Scores')
fig, ax = plt.subplots()
sns.histplot(df['price_z'], bins=10, kde=True, ax=ax)
st.pyplot(fig)

# Aggregate data
agg_data = df.groupby(['country', 'room_type']).agg({'price': 'mean'}).reset_index()

# Plotly bar plot
st.subheader('Average Price by Country and Room Type')
fig = px.bar(agg_data, x='country', y='price', color='room_type', barmode='group',
             labels={'price': 'Average Price', 'country': 'Country', 'room_type': 'Room Type'},
             title='Average Price by Country and Room Type')
st.plotly_chart(fig)
