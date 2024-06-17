import streamlit as st
import pandas as pd

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

df['price_z']=round((df['price']-df['price'].mean())/df['price'].std(),2)
df=df[(df['price_z']<=3) & (df['price_z']>=-3)]


#summary stats
st.write('### Summary Statistics')
df1=df.describe()
df1=df1.drop("count",axis=0)
df1['price']