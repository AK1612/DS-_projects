import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

st.title("Top 10")

cl=mysql.connector.connect(host="localhost",
                           user="root",
                           password="root",
                           database="phonepe")
cursor=cl.cursor()

options_1=["","2018","2019","2020","2021","2022","2023","2024"]
options_2=["","1st","2nd","3rd","4th"]
options_3=["","District","pincode"]
options_4=["","Transactions","Users"]

option_1=st.selectbox("Select Year",options_1)
option_2=st.selectbox("Select Quarter",options_2)
option_3=st.selectbox("Select District/pincode",options_3)
option_4=st.selectbox("Select Type",options_4)
if option_1=="2018":
    if option_2=="1st":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2018' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2018' and Quater='1' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2018' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2018' and Quater='1' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="2nd":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2018' and Quater='2' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2018' and Quater='2' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2018' and Quater='2' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2018' and Quater='2' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="3rd":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2018' and Quater='3' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2018' and Quater='3' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2018' and Quater='3' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2018' and Quater='3' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="4th":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2018' and Quater='4' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2018' and Quater='4' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2018' and Quater='4' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2018' and Quater='4' order by registered_users desc limit 10",cl)
                    df
elif option_1=="2019":
    if option_2=="1st":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2019' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2019' and Quater='1' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2019' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2019' and Quater='1' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="2nd":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2019' and Quater='2' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2019' and Quater='2' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2019' and Quater='2' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2019' and Quater='2' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="3rd":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2019' and Quater='3' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2019' and Quater='3' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2019' and Quater='3' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2019' and Quater='3' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="4th":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2019' and Quater='4' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2019' and Quater='4' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2019' and Quater='4' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2019' and Quater='4' order by registered_users desc limit 10",cl)
                    df
elif option_1=="2020":
    if option_2=="1st":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2020' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2020' and Quater='1' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2020' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2020' and Quater='1' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="2nd":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2020' and Quater='2' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2020' and Quater='2' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2020' and Quater='2' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2020' and Quater='2' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="3rd":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2020' and Quater='3' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2020' and Quater='3' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2020' and Quater='3' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2020' and Quater='3' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="4th":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2020' and Quater='4' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2020' and Quater='4' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2020' and Quater='4' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2020' and Quater='4' order by registered_users desc limit 10",cl)
                    df
elif option_1=="2021":
    if option_2=="1st":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2021' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2021' and Quater='1' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2021' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2021' and Quater='1' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="2nd":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2021' and Quater='2' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2021' and Quater='2' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2021' and Quater='2' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2021' and Quater='2' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="3rd":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2021' and Quater='3' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2021' and Quater='3' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2021' and Quater='3' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2021' and Quater='3' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="4th":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2021' and Quater='4' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2021' and Quater='4' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2021' and Quater='4' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2021' and Quater='4' order by registered_users desc limit 10",cl)
                    df
elif option_1=="2022":
    if option_2=="1st":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2022' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2022' and Quater='1' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2022' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2022' and Quater='1' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="2nd":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2022' and Quater='2' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2022' and Quater='2' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2022' and Quater='2' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2022' and Quater='2' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="3rd":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2022' and Quater='3' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2022' and Quater='3' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2022' and Quater='3' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2022' and Quater='3' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="4th":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2022' and Quater='4' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2022' and Quater='4' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2022' and Quater='4' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2022' and Quater='4' order by registered_users desc limit 10",cl)
                    df
elif option_1=="2023":
    if option_2=="1st":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2023' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2023' and Quater='1' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2023' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2023' and Quater='1' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="2nd":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2023' and Quater='2' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2023' and Quater='2' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2023' and Quater='2' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2023' and Quater='2' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="3rd":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2023' and Quater='3' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2023' and Quater='3' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2023' and Quater='3' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2023' and Quater='3' order by registered_users desc limit 10",cl)
                    df
    elif option_2=="4th":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2023' and Quater='4' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2023' and Quater='4' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2023' and Quater='4' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2023' and Quater='4' order by registered_users desc limit 10",cl)
                    df
elif option_1=="2024":
    if option_2=="1st":
        if option_3=="District":
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_d")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,District,count,Amount from top_trans_d where Year='2024' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_d")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,District,Registered_users from top_users_d where Year='2024' and Quater='1' order by registered_users desc limit 10",cl)
                    df
        else:
            if option_4=="Transactions":
               if st.button("get"):
                   cursor.execute("show columns from top_trans_p")
                   mcl=cursor.fetchall()
                   df=pd.DataFrame(mcl)
                   df=pd.read_sql("select Year,Quater,Pincode,count,Amount from top_trans_d where Year='2024' and Quater='1' order by Amount desc limit 10",cl)
                   df
            else:
                if st.button("get"):
                    cursor.execute("show columns from top_users_p")
                    mcl=cursor.fetchall()
                    df=pd.DataFrame(mcl)
                    df=pd.read_sql("select Year,Quater,Pincode,Registered_users from top_users_d where Year='2024' and Quater='1' order by registered_users desc limit 10",cl)
                    df

