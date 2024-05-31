import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

st.title("Queries")

cl=mysql.connector.connect(host="localhost",
                           user="root",
                           password="root",
                           database="phonepe")
cursor=cl.cursor()

options=["which state has large coustomer base over the years?",
         "total no of recharges in 2019?",
        "which state contributed more in financial services in 2021?",
        "how many app opens are converted into one transaction over the years?",
        "transaction amount per registered users over the years?"]

option=st.selectbox("Select Queries",options)

if option=="which state has large coustomer base over the years?":
    if st.button("get"):
      cursor.execute("show columns from agg_users")
      mcl=cursor.fetchall()
      dfi=pd.DataFrame(mcl)
      dfi=pd.read_sql("select State, sum(Count) from agg_users group by State order by sum(Count) desc limit 1",cl)
      dfi.rename(columns={"sum(Count)": "count"}, inplace=True)
      dfi
elif option=="total no of recharges in 2019?":
    if st.button("get"):
       cursor.execute("show columns from agg_trans")
       mcl=cursor.fetchall()
       dfi=pd.DataFrame(mcl)
       dfi=pd.read_sql("select Year, Transaction_type, sum(Transaction_count) from agg_trans where Transaction_type='Recharge & bill payments' and Year='2019' group by Year,Transaction_type order by sum(Transaction_count) desc limit 1",cl)
       dfi.rename(columns={"sum(Transaction_count)": "Transaction_count"}, inplace=True)
       dfi['Transaction_count']
elif option=="which state contributed more in financial services in 2021?":
    if st.button("get"):
       cursor.execute("show columns from agg_trans")
       mcl=cursor.fetchall()
       dfi=pd.DataFrame(mcl)
       dfi=pd.read_sql("select Year,State, Transaction_type, sum(Transaction_count) from agg_trans where Transaction_type='Financial Services' and Year='2021' group by Year,State,Transaction_type order by sum(Transaction_count) desc limit 1",cl)
       dfi.rename(columns={"sum(Transaction_count)": "Transaction_count"}, inplace=True)
       dfi
elif option=="how many app opens are converted into one transaction over the years?":
    if st.button("get"):
       cursor.execute("show columns from map_trans")
       ml=cursor.fetchall()
       d=pd.DataFrame(ml)
       d=pd.read_sql("select Year, sum(Count), sum(Amount) from map_trans where year>2018 group by Year",cl)
       d.rename(columns={"sum(Count)": "Count"}, inplace=True)
       d.rename(columns={"sum(Amount)": "Amount"}, inplace=True)
       cursor.execute("show columns from map_users")
       mcl=cursor.fetchall()
       df=pd.DataFrame(mcl)
       df=pd.read_sql("select Year, sum(Registered_users), sum(App_opens) from map_users where year!=2018 group by Year",cl)
       df.rename(columns={"sum(Registered_users)": "Registered_users"}, inplace=True)
       df.rename(columns={"sum(App_opens)": "App_opens"}, inplace=True)
       merged_df = pd.merge(d, df, on=['Year'])
       count_vs_appopens = merged_df[['Year', 'App_opens', 'Count']]
       count_vs_appopens["appopens per transaction"]=count_vs_appopens["App_opens"]/count_vs_appopens["Count"]
       count_vs_appopens  
elif option=="transaction amount per registered users over the years?":
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
       merged_df = pd.merge(d, df, on=['Year'])
       amount_vs_users = merged_df[['Year', 'Registered_users', 'Amount']]
       amount_vs_users["transamount per user"]=amount_vs_users["Amount"]/amount_vs_users["Registered_users"]
       amount_vs_users
