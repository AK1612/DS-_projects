import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

st.title("Geo Visualisation")
import pandas as pd
import json
import os

path="C:\\Users\\SHREE\\OneDrive\\Documents\\GitHub\\pulse\\data\\aggregated\\transaction\\country\\india\\state\\"
Agg_state_list=os.listdir(path)
clm={'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}

for i in Agg_state_list:
    p_i=path+i+"\\"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"\\"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              amount=amount/(10**7)
              clm['Transacion_type'].append(Name)
              clm['Transacion_count'].append(count)
              clm['Transacion_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))
#Succesfully created a dataframe
Agg_Trans=pd.DataFrame(clm)

# %%
p="C:\\Users\\SHREE\\OneDrive\\Documents\\GitHub\\pulse\\data\\aggregated\\user\\country\\india\\state\\"
state_list=os.listdir(p)

# %%
users={'State':[], 'Year':[],'Quater':[],'Brand':[], 'Count':[], 'Percentage':[]}

for i in state_list:
    p_i=p+i+"\\"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"\\"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            u=open(p_k,'r')
            q=json.load(u)
            if q['data']['usersByDevice']!=None:
                for z in q['data']['usersByDevice']:
                  B=z['brand']
                  count=z['count']
                  percentage=z['percentage']
                  users['Brand'].append(B)
                  users['Count'].append(count)
                  users['Percentage'].append(percentage)
                  users['State'].append(i)
                  users['Year'].append(j)
                  users['Quater'].append(int(k.strip('.json')))
            else:
                continue
#Succesfully created a dataframe
Agg_users=pd.DataFrame(users)

# %%
x="C:\\Users\\SHREE\\OneDrive\\Documents\\GitHub\\pulse\\data\\map\\transaction\\hover\\country\\india\\state\\"
y=os.listdir(x)

# %%
map_trans={'State':[], 'Year':[],'Quater':[],'District':[], 'Count':[], 'Amount':[]}

for i in y:
    p_i=x+i+"\\"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"\\"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['hoverDataList']:
              district=z['name']
              count=z['metric'][0]['count']
              amount=z['metric'][0]['amount']
              amount=amount/(10**7)
              map_trans['District'].append(district)
              map_trans['Count'].append(count)
              map_trans['Amount'].append(amount)
              map_trans['State'].append(i)
              map_trans['Year'].append(j)
              map_trans['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
map_t=pd.DataFrame(map_trans)

# %%
pa="C:\\Users\\SHREE\\OneDrive\\Documents\\GitHub\\pulse\\data\\map\\user\\hover\\country\\india\\state\\"
e=os.listdir(pa)

# %%
map_users={'State':[], 'Year':[],'Quater':[],'District':[], 'Registered_users':[], 'App_opens':[]}

for i in e:
    p_i=pa+i+"\\"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"\\"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['hoverData']:
              district=z
              registered_Users=D['data']['hoverData'][z]['registeredUsers']
              app_opens=D['data']['hoverData'][z]['appOpens']
              map_users['District'].append(district)
              map_users['Registered_users'].append(registered_Users)
              map_users['App_opens'].append(app_opens)
              map_users['State'].append(i)
              map_users['Year'].append(j)
              map_users['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
map_u=pd.DataFrame(map_users)

# %%
pat="C:\\Users\\SHREE\\OneDrive\\Documents\\GitHub\\pulse\\data\\top\\transaction\\country\\india\\state\\"
ex=os.listdir(pat)

# %%
top_trans={'State':[], 'Year':[],'Quater':[],'District':[], 'Count':[], 'Amount':[]}

for i in ex:
    p_i=pat+i+"\\"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"\\"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['districts']:
              district=z['entityName']
              count=z['metric']['count']
              amount=z['metric']['amount']
              amount=amount/(10**7)
              top_trans['District'].append(district)
              top_trans['Count'].append(count)
              top_trans['Amount'].append(amount)
              top_trans['State'].append(i)
              top_trans['Year'].append(j)
              top_trans['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
top_t_D=pd.DataFrame(top_trans)

# %%
top_trans_pin={'State':[], 'Year':[],'Quater':[],'Pincode':[], 'Count':[], 'Amount':[]}

for i in ex:
    p_i=pat+i+"\\"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"\\"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['pincodes']:
              pin=z['entityName']
              count=z['metric']['count']
              amount=z['metric']['amount']
              amount=amount/(10**7)
              top_trans_pin['Pincode'].append(pin)
              top_trans_pin['Count'].append(count)
              top_trans_pin['Amount'].append(amount)
              top_trans_pin['State'].append(i)
              top_trans_pin['Year'].append(j)
              top_trans_pin['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
top_t_p=pd.DataFrame(top_trans_pin)

# %%
pah="C:\\Users\\SHREE\\OneDrive\\Documents\\GitHub\\pulse\\data\\top\\user\\country\\india\\state\\"
pl=os.listdir(pah)

# %%
top_users_dit={'State':[], 'Year':[],'Quater':[],'District':[], 'Registered_users':[]}

for i in pl:
    p_i=pah+i+"\\"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"\\"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            a=json.load(Data)
            for z in a['data']['districts']:
              dt=z['name']
              re_us=z['registeredUsers']
              top_users_dit['District'].append(dt)
              top_users_dit['Registered_users'].append(re_us)
              top_users_dit['State'].append(i)
              top_users_dit['Year'].append(j)
              top_users_dit['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
top_u_d=pd.DataFrame(top_users_dit)

# %%
top_users_pin={'State':[], 'Year':[],'Quater':[],'Pincode':[], 'Registered_users':[]}

for i in pl:
    p_i=pah+i+"\\"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"\\"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            a=json.load(Data)
            for z in a['data']['pincodes']:
              po=z['name']
              re_us=z['registeredUsers']
              top_users_pin['Pincode'].append(po)
              top_users_pin['Registered_users'].append(re_us)
              top_users_pin['State'].append(i)
              top_users_pin['Year'].append(j)
              top_users_pin['Quater'].append(int(k.strip('.json')))

#Succesfully created a dataframe
top_u_p=pd.DataFrame(top_users_pin)

# inserting data frame into table in database using sqlalchemy
import mysql.connector
from sqlalchemy import create_engine
client=create_engine("mysql://root:root@localhost/phonepe")
Agg_Trans.to_sql("agg_trans",client,if_exists="replace")
Agg_users.to_sql("agg_users",client,if_exists="replace")
map_t.to_sql("map_trans",client,if_exists="replace")
map_u.to_sql("map_users",client,if_exists="replace")
top_t_D.to_sql("top_trans_d",client,if_exists="replace")
top_t_p.to_sql("top_trans_p",client,if_exists="replace")
top_u_d.to_sql("top_users_d",client,if_exists="replace")
top_u_p.to_sql("top_users_p",client,if_exists="replace")

cl=mysql.connector.connect(host="localhost",
                           user="root",
                           password="root",
                           database="phonepe")
cursor=cl.cursor()
cursor.execute("update map_users set State='Andaman & Nicobar' where State='andaman-&-nicobar-islands'")
cursor.execute("update map_users set State='Andhra Pradesh' where State='andhra-pradesh'")
cursor.execute("update map_users set State='Arunachal Pradesh' where State='arunachal-pradesh'")
cursor.execute("update map_users set State='Assam' where State='assam'")
cursor.execute("update map_users set State='Bihar' where State='bihar'")
cursor.execute("update map_users set State='Chandigarh' where State='chandigarh'")
cursor.execute("update map_users set State='Chhattisgarh' where State='chhattisgarh'")
cursor.execute("update map_users set State='Dadra and Nagar Haveli and Daman and Diu' where State='dadra-&-nagar-haveli-&-daman-&-diu'")
cursor.execute("update map_users set State='Delhi' where State='delhi'")
cursor.execute("update map_users set State='Goa' where State='goa'")
cursor.execute("update map_users set State='Gujarat' where State='gujarat'")
cursor.execute("update map_users set State='Haryana' where State='haryana'")
cursor.execute("update map_users set State='Himachal Pradesh' where State='himachal-pradesh'")
cursor.execute("update map_users set State='Jammu & Kashmir' where State='jammu-&-kashmir'")
cursor.execute("update map_users set State='Jharkhand' where State='jharkhand'")
cursor.execute("update map_users set State='Karnataka' where State='karnataka'")
cursor.execute("update map_users set State='Kerala' where State='kerala'")
cursor.execute("update map_users set State='Ladakh' where State='ladakh'")
cursor.execute("update map_users set State='Madhya Pradesh' where State='madhya-pradesh'")
cursor.execute("update map_users set State='Maharashtra' where State='maharashtra'")
cursor.execute("update map_users set State='Manipur' where State='manipur'")
cursor.execute("update map_users set State='Meghalaya' where State='meghalaya'")
cursor.execute("update map_users set State='Mizoram' where State='mizoram'")
cursor.execute("update map_users set State='Nagaland' where State='nagaland'")
cursor.execute("update map_users set State='Odisha' where State='odisha'")
cursor.execute("update map_users set State='Puducherry' where State='puducherry'")
cursor.execute("update map_users set State='Punjab' where State='punjab'")
cursor.execute("update map_users set State='Rajasthan' where State='rajasthan'")
cursor.execute("update map_users set State='Sikkim' where State='sikkim'")
cursor.execute("update map_users set State='Tamil Nadu' where State='tamil-nadu'")
cursor.execute("update map_users set State='Telangana' where State='telangana'")
cursor.execute("update map_users set State='Tripura' where State='tripura'")
cursor.execute("update map_users set State='Uttarakhand' where State='uttarakhand'")
cursor.execute("update map_users set State='Uttar Pradesh' where State='uttar-pradesh'")
cursor.execute("update map_users set State='West Bengal' where State='west-bengal'")
cl.commit()


cursor.execute("update map_trans set State='Andaman & Nicobar' where State='andaman-&-nicobar-islands'")
cursor.execute("update map_trans set State='Andhra Pradesh' where State='andhra-pradesh'")
cursor.execute("update map_trans set State='Arunachal Pradesh' where State='arunachal-pradesh'")
cursor.execute("update map_trans set State='Assam' where State='assam'")
cursor.execute("update map_trans set State='Bihar' where State='bihar'")
cursor.execute("update map_trans set State='Chandigarh' where State='chandigarh'")
cursor.execute("update map_trans set State='Chhattisgarh' where State='chhattisgarh'")
cursor.execute("update map_trans set State='Dadra and Nagar Haveli and Daman and Diu' where State='dadra-&-nagar-haveli-&-daman-&-diu'")
cursor.execute("update map_trans set State='Delhi' where State='delhi'")
cursor.execute("update map_trans set State='Goa' where State='goa'")
cursor.execute("update map_trans set State='Gujarat' where State='gujarat'")
cursor.execute("update map_trans set State='Haryana' where State='haryana'")
cursor.execute("update map_trans set State='Himachal Pradesh' where State='himachal-pradesh'")
cursor.execute("update map_trans set State='Jammu & Kashmir' where State='jammu-&-kashmir'")
cursor.execute("update map_trans set State='Jharkhand' where State='jharkhand'")
cursor.execute("update map_trans set State='Karnataka' where State='karnataka'")
cursor.execute("update map_trans set State='Kerala' where State='kerala'")
cursor.execute("update map_trans set State='Ladakh' where State='ladakh'")
cursor.execute("update map_trans set State='Madhya Pradesh' where State='madhya-pradesh'")
cursor.execute("update map_trans set State='Maharashtra' where State='maharashtra'")
cursor.execute("update map_trans set State='Manipur' where State='manipur'")
cursor.execute("update map_trans set State='Meghalaya' where State='meghalaya'")
cursor.execute("update map_trans set State='Mizoram' where State='mizoram'")
cursor.execute("update map_trans set State='Nagaland' where State='nagaland'")
cursor.execute("update map_trans set State='Odisha' where State='odisha'")
cursor.execute("update map_trans set State='Puducherry' where State='puducherry'")
cursor.execute("update map_trans set State='Punjab' where State='punjab'")
cursor.execute("update map_trans set State='Rajasthan' where State='rajasthan'")
cursor.execute("update map_trans set State='Sikkim' where State='sikkim'")
cursor.execute("update map_trans set State='Tamil Nadu' where State='tamil-nadu'")
cursor.execute("update map_trans set State='Telangana' where State='telangana'")
cursor.execute("update map_trans set State='Tripura' where State='tripura'")
cursor.execute("update map_trans set State='Uttarakhand' where State='uttarakhand'")
cursor.execute("update map_trans set State='Uttar Pradesh' where State='uttar-pradesh'")
cursor.execute("update map_trans set State='West Bengal' where State='west-bengal'")
cl.commit()

options_1=["","2018","2019","2020","2021","2022","2023","2024"]
options_2=["","1st","2nd","3rd","4th"]
options_3=["","Transactions","Users"]

option_1=st.selectbox("Select Year",options_1)
option_2=st.selectbox("Select Quarter",options_2)
option_3=st.selectbox("Select Type",options_3)

if option_1=="2018":
    if option_2=="1st":
        if option_3=="Transactions":
           if st.button("get"):
               cursor.execute("show columns from map_trans")
               mcl=cursor.fetchall()
               df=pd.DataFrame(mcl)
               df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2018'and Quater='1' group by Year,Quater,State",cl)
               fig = px.choropleth(
                                   df,
                                   geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                   featureidkey='properties.ST_NM',
                                   locations="State",
                                   color="sum(Amount)",hover_data=['Year','sum(Count)'],
                                   color_continuous_scale='dense')

               fig.update_geos(fitbounds="locations", visible=False)

               fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2018'and Quater='1' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="2nd":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2018'and Quater='2' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2018'and Quater='2' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="3rd":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2018'and Quater='3' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2018'and Quater='3' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="4th":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2018'and Quater='4' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2018'and Quater='4' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

elif option_1=="2019":
    if option_2=="1st":
        if option_3=="Transactions":
           if st.button("get"):
               cursor.execute("show columns from map_trans")
               mcl=cursor.fetchall()
               df=pd.DataFrame(mcl)
               df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2019'and Quater='1' group by Year,Quater,State",cl)
               fig = px.choropleth(
                                   df,
                                   geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                   featureidkey='properties.ST_NM',
                                   locations="State",
                                   color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                   color_continuous_scale='dense')

               fig.update_geos(fitbounds="locations", visible=False)

               fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2019'and Quater='1' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="2nd":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2019'and Quater='2' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2019'and Quater='2' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="3rd":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2019'and Quater='3' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2019'and Quater='3' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="4th":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2019'and Quater='4' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2019'and Quater='4' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

elif option_1=="2020":
    if option_2=="1st":
        if option_3=="Transactions":
           if st.button("get"):
               cursor.execute("show columns from map_trans")
               mcl=cursor.fetchall()
               df=pd.DataFrame(mcl)
               df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2020'and Quater='1' group by Year,Quater,State",cl)
               fig = px.choropleth(
                                   df,
                                   geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                   featureidkey='properties.ST_NM',
                                   locations="State",
                                   color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                   color_continuous_scale='dense')

               fig.update_geos(fitbounds="locations", visible=False)

               fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2020'and Quater='1' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="2nd":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2020'and Quater='2' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2020'and Quater='2' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="3rd":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2020'and Quater='3' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2020'and Quater='3' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="4th":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2020'and Quater='4' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2020'and Quater='4' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

elif option_1=="2021":
    if option_2=="1st":
        if option_3=="Transactions":
           if st.button("get"):
               cursor.execute("show columns from map_trans")
               mcl=cursor.fetchall()
               df=pd.DataFrame(mcl)
               df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2021'and Quater='1' group by Year,Quater,State",cl)
               fig = px.choropleth(
                                   df,
                                   geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                   featureidkey='properties.ST_NM',
                                   locations="State",
                                   color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                   color_continuous_scale='dense')

               fig.update_geos(fitbounds="locations", visible=False)

               fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2021'and Quater='1' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="2nd":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2021'and Quater='2' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2021'and Quater='2' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="3rd":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2021'and Quater='3' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2021'and Quater='3' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="4th":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2021'and Quater='4' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2021'and Quater='4' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

elif option_1=="2022":
    if option_2=="1st":
        if option_3=="Transactions":
           if st.button("get"):
               cursor.execute("show columns from map_trans")
               mcl=cursor.fetchall()
               df=pd.DataFrame(mcl)
               df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2022'and Quater='1' group by Year,Quater,State",cl)
               fig = px.choropleth(
                                   df,
                                   geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                   featureidkey='properties.ST_NM',
                                   locations="State",
                                   color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                   color_continuous_scale='dense')

               fig.update_geos(fitbounds="locations", visible=False)

               fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2022'and Quater='1' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="2nd":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2022'and Quater='2' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2022'and Quater='2' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="3rd":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2022'and Quater='3' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2022'and Quater='3' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="4th":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2022'and Quater='4' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2022'and Quater='4' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

elif option_1=="2023":
    if option_2=="1st":
        if option_3=="Transactions":
           if st.button("get"):
               cursor.execute("show columns from map_trans")
               mcl=cursor.fetchall()
               df=pd.DataFrame(mcl)
               df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2023'and Quater='1' group by Year,Quater,State",cl)
               fig = px.choropleth(
                                   df,
                                   geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                   featureidkey='properties.ST_NM',
                                   locations="State",
                                   color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                   color_continuous_scale='dense')

               fig.update_geos(fitbounds="locations", visible=False)

               fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2023'and Quater='1' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="2nd":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2023'and Quater='2' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2023'and Quater='2' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="3rd":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2023'and Quater='3' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2023'and Quater='3' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

    elif option_2=="4th":
        if option_3=="Transactions":
            if st.button("get"):
                cursor.execute("show columns from map_trans")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2023'and Quater='4' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2023'and Quater='4' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()

elif option_1=="2024":
    if option_2=="1st":
        if option_3=="Transactions":
           if st.button("get"):
               cursor.execute("show columns from map_trans")
               mcl=cursor.fetchall()
               df=pd.DataFrame(mcl)
               df=pd.read_sql("select Year, Quater, State, sum(Count), sum(Amount) from map_trans where Year='2024'and Quater='1' group by Year,Quater,State",cl)
               fig = px.choropleth(
                                   df,
                                   geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                   featureidkey='properties.ST_NM',
                                   locations="State",
                                   color="sum(Amount)",hover_data=['Year', 'sum(Count)'],
                                   color_continuous_scale='dense')

               fig.update_geos(fitbounds="locations", visible=False)

               fig.show()
        else:
            if st.button("get"):
                cursor.execute("show columns from map_users")
                mcl=cursor.fetchall()
                df=pd.DataFrame(mcl)
                df=pd.read_sql("select Year, Quater, State, sum(Registered_users), sum(App_opens) from map_users where Year='2024'and Quater='1' group by Year,Quater,State",cl)
                fig = px.choropleth(
                                    df,
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    featureidkey='properties.ST_NM',
                                    locations="State",
                                    color="sum(Registered_users)",hover_data=['Year','sum(App_opens)'],
                                    color_continuous_scale='dense')

                fig.update_geos(fitbounds="locations", visible=False)

                fig.show()
