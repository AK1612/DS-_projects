import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

st.title("Data Visualisation")

cl=mysql.connector.connect(host="localhost",
                           user="root",
                           password="root",
                           database="phonepe")
cursor=cl.cursor()

options=["Show the relation between registered users and transaction amount",
         "Show the relation between app opens and transaction count",
         "show Transaction types contributed to Revenue",
         "show transaction types contributed to transaction count"]

option=st.selectbox("Select",options)

if option=="Show the relation between registered users and transaction amount":
    if st.button("get"):
       cursor.execute("show columns from map_trans")
       ml=cursor.fetchall()
       d=pd.DataFrame(ml)
       d=pd.read_sql("select Year, sum(Count), sum(Amount) from map_trans group by Year",cl)
       d.rename(columns={"sum(Count)": "Count"}, inplace=True)
       d.rename(columns={"sum(Amount)": "Amount"}, inplace=True)
       cursor.execute("show columns from map_users")
       mcl=cursor.fetchall()
       df=pd.DataFrame(mcl)
       df=pd.read_sql("select Year, sum(Registered_users), sum(App_opens) from map_users group by Year",cl)
       df.rename(columns={"sum(Registered_users)": "Registered_users"}, inplace=True)
       df.rename(columns={"sum(App_opens)": "App_opens"}, inplace=True)

       merged_df= pd.merge(d, df, on=['Year'])
       amount_vs_registered_users = merged_df[['Year', 'Amount', 'Registered_users']]
       fig = px.bar(amount_vs_registered_users, x='Year', y='Amount',
                    hover_data=['Registered_users'], color='Registered_users',
                    labels={'Amount':'transaction Amount'}, height=500)
       st.plotly_chart(fig, use_container_width=True,theme=None)
elif option=="Show the relation between app opens and transaction count":
    if st.button("get"):
       cursor.execute("show columns from map_trans")
       ml=cursor.fetchall()
       d=pd.DataFrame(ml)
       d=pd.read_sql("select Year, sum(Count), sum(Amount) from map_trans group by Year",cl)
       d.rename(columns={"sum(Count)": "Count"}, inplace=True)
       d.rename(columns={"sum(Amount)": "Amount"}, inplace=True)
       cursor.execute("show columns from map_users")
       mcl=cursor.fetchall()
       df=pd.DataFrame(mcl)
       df=pd.read_sql("select Year, sum(Registered_users), sum(App_opens) from map_users group by Year",cl)
       df.rename(columns={"sum(Registered_users)": "Registered_users"}, inplace=True)
       df.rename(columns={"sum(App_opens)": "App_opens"}, inplace=True)

       merged_df= pd.merge(d, df, on=['Year'])
       count_vs_app_opens = merged_df[['Year', 'Count', 'App_opens']]
       fig = px.bar(count_vs_app_opens, x='Year', y='Count',
                    hover_data=['App_opens'], color='App_opens',
                    labels={'Count':'transaction Count'}, height=500)
       st.plotly_chart(fig, use_container_width=True,theme=None)
elif option=="show Transaction types contributed to Revenue":
    if st.button("get"):
       cursor.execute("show columns from agg_trans")
       mcl=cursor.fetchall()
       dfi=pd.DataFrame(mcl)
       dfi=pd.read_sql("select Year, Transaction_type, sum(Transaction_Amount) from agg_trans group by Year,Transaction_type",cl)
       dfi.rename(columns={"sum(Transaction_Amount)": "Transaction_Amount"}, inplace=True)
       fig = px.line(dfi, x="Year", y="Transaction_Amount", color='Transaction_type',markers='Year')
       st.plotly_chart(fig, use_container_width=True,theme=None)
elif option=="show transaction types contributed to transaction count":
    if st.button("get"):
      cursor.execute("show columns from agg_trans")
      mcl=cursor.fetchall()
      dfi=pd.DataFrame(mcl)
      dfi=pd.read_sql("select Year, Transaction_type, sum(Transaction_count) from agg_trans group by Year,Transaction_type",cl)
      dfi.rename(columns={"sum(Transaction_count)": "Transaction_count"}, inplace=True)
      fig = px.line(dfi, x="Year", y="Transaction_count", color='Transaction_type',markers='Year')
      st.plotly_chart(fig, use_container_width=True,theme=None)
          
      








