import re
import streamlit as st
import mysql.connector
import pandas as pd
import googleapiclient.discovery

#youtube API connectivity:

api_service_name = "youtube"
api_version = "v3"
api_key="AIzaSyDjnu1Ohxk-rK8DvD8g6B2HAqkeBKke12U" #insert API key here
youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

#Step 1: Getting channel details using channel id given by user
comm_data=[]
cha_data=[]
data_pla=[]
data_video=[]
v_data=[]

def ybe(c_id):
    request = youtube.channels().list(part="snippet,contentDetails,statistics", id=c_id)
    response = request.execute()
    cha_data.insert(0,[response['items'][0]['id'],response['items'][0]['snippet']['title'],
                       response['items'][0]['statistics']['viewCount'],
                       response['items'][0]['snippet']['description']])
    cha_data[0][2]=int(cha_data[0][2])
    cha_data[0]=tuple(cha_data[0])
    client=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="proj_dsa")
    cursor=client.cursor()
    query="""insert into channel (channel_id,
           channel_name, channel_views, channel_description) values (%s, %s, %s, %s)"""
    cursor.execute(query,cha_data[0])
    client.commit()
    return cha_data

#Step 2:Getting playlist details using channel id

def pla(p):
    request = youtube.playlists().list(part="snippet,contentDetails",channelId=p,maxResults=50)
    response = request.execute()
    x=len(response['items'])

    for i in range(x):
        data_pla.insert(i,(response['items'][i]['id'],response['items'][0]['snippet']['channelId'],
                           response['items'][i]['snippet']['title']))
    client=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="proj_dsa")
    cursor=client.cursor()
    query="insert into playlist values(%s, %s, %s)"
    cursor.execute(query,data_pla[0])
    client.commit()
    return data_pla

#Step 3:Getting video details using playlist id

def vid(x):
    data_video=[]
    for i in range(x):
        request = youtube.playlistItems().list(part="snippet,contentDetails",
                                               playlistId=data_pla[i][0],maxResults=50)
        response=request.execute()
        for h in range(len(response['items'])):
            j=len(data_video)
            data_video.insert(j,[response['items'][h]['snippet']['resourceId']['videoId'],data_pla[i][0],
                                 response['items'][h]['snippet']['title'],response['items'][h]['snippet']['description']])
    
    count_video=[]
    er=[]
    s=0
    r=len(data_video)
    for k in range(r):
        request=youtube.videos().list(part="snippet,contentDetails,statistics",id=data_video[k][0])
        response=request.execute()
        #For eliminating deleted video details from the list
        if len(response['items'])==0:
            er.insert(s,k)
            s=s+1
        else:
            for m in range(len(response['items'])):
                count_video.insert(m,[response['items'][0]['statistics']['viewCount'],response['items'][0]['statistics']['likeCount'],
                                      response['items'][0]['statistics']['favoriteCount'],response['items'][0]['statistics']['commentCount'],
                                      response['items'][0]['contentDetails']['duration'],response['items'][0]['snippet']['thumbnails']['default']['url'],
                                      response['items'][0]['snippet']['publishedAt']])
    if len(er)!=0:
        for q in range(len(er)):
            del data_video[er[q]]
#data cleaning
    for i in range(len(count_video)):
        x=count_video[i][6].replace('T'," ")
        count_video[i][6]=x.replace('Z',"")
        count_video[i].insert(7,count_video[i][6][0:4])
        count_video[i][0]=int(count_video[i][0])
        count_video[i][1]=int(count_video[i][1])
        count_video[i][2]=int(count_video[i][2])
        count_video[i][3]=int(count_video[i][3])


    def YTDurationToSeconds(duration):
        match = re.match('PT(\d+H)?(\d+M)?(\d+S)?',duration ).groups()
        hours = _js_parseInt(match[0]) if match[0] else 0
        minutes = _js_parseInt(match[1]) if match[1] else 0
        seconds = _js_parseInt(match[2]) if match[2] else 0
        h=hours * 3600 + minutes * 60 + seconds
        return h

    def _js_parseInt(string):
        return int(''.join([x for x in string if x.isdigit()]))
   
    for i in range(len(count_video)):
        count_video[i][4]=YTDurationToSeconds(count_video[i][4])
        v_data.insert(i,(data_video[i] + count_video[i]))
        v_data[i]=tuple(v_data[i])
    client=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="proj_dsa")
    cursor=client.cursor()

    query="insert into video values(%s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s, %s)"
    cursor.executemany(query,v_data)
    client.commit()
    return v_data

#Step 4:Getting comment details of each video using video id

def comm(t):
    for g in range(t):
        request = youtube.commentThreads().list(part="snippet,replies",videoId=v_data[g][0],maxResults=10)
        response=request.execute()
        for z in range(len(response['items'])):
            d=len(comm_data)
            comm_data.insert(d,[response['items'][z]['snippet']['topLevelComment']['id'],v_data[g][0],
                                response['items'][z]['snippet']['topLevelComment']['snippet']['textDisplay'],
                                response['items'][z]['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                                response['items'][z]['snippet']['topLevelComment']['snippet']['publishedAt']])
    for i in range(len(comm_data)):
        x=comm_data[i][4].replace('T'," ")
        comm_data[i][4]=x.replace('Z',"")
        comm_data[i]=tuple(comm_data[i])
    
    client=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="proj_dsa")
    cursor=client.cursor()


    query="insert into comment values(%s, %s, %s, %s, %s)"
    cursor.executemany(query,comm_data)
    client.commit()
    return comm_data



add_selectbox=st.sidebar.selectbox("select options",("HOME","DATA ETRACTION","QUERIES"))

if add_selectbox=="HOME":
    st.title('YOUTUBE DATA HARVESTING')
if add_selectbox=="DATA ETRACTION":
    j=st.text_input("Enter the Channel id",None)
    if (st.button("extract")):
       ybe(j)
       pla(cha_data[0][0])
       vid(len(data_pla))
       comm(len(v_data))

if add_selectbox=="QUERIES":

    options = ["What are the Names of all the videos and their corresponding channels?",
                "Which channels have the most number of videos, and how many videos do they have?",
                "What are the top 10 most viewed videos and their respective channels ?",
                "How many comments were made on each video, and what are their corresponding video names?",
                "Which videos have the highest number of likes, and what are their corresponding channel names?",
                "What is the total number of likes for each video, and what are  their corresponding video names?",
                "What is the total number of views for each channel, and what are their corresponding channel names?",
                "What are the names of all the channels that have published videos in the year 2022?",
                "What is the average duration of all videos in each channel, and what are their corresponding channel names?",
                "Which videos have the highest number of comments, and what are their corresponding channel names?"]

    option = st.selectbox('Select Question', options)
    
    
    # 1
    if option == "What are the Names of all the videos and their corresponding channels?":
        if st.button("GET SOLUTION"):
            client=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="proj_DSA")
            cursor=client.cursor()
    
            query = """select channel.channel_name  , video.video_name 
                       from channel inner join playlist on channel.channel_id=playlist.channel_id 
                       inner join video on playlist.playlist_id=video.playlist_id order by channel.channel_name"""
            cursor.execute(query)
            data_1 = [i for i in cursor.fetchall()]
            st.dataframe(pd.DataFrame(data_1, columns=["Channel Name", "Video Title"], index=range(1, len(data_1) + 1)))
            st.success("DONE")
    
# 2
    elif option == "Which channels have the most number of videos, and how many videos do they have?":
         if st.button("GET SOLUTION"):
            client=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="proj_dsa")
            cursor=client.cursor()

            query_2 = """select  channel.channel_name , count(video.video_name)   from channel inner join playlist on channel.channel_id=playlist.channel_id 
                             inner join video on playlist.playlist_id=video.playlist_id group by channel.channel_name
                             order by count(video.video_name) desc limit 1"""
            cursor.execute(query_2)
            print("Channel with Most number of Videos :")
            data_2 = [i for i in cursor.fetchall()]
            df_1 = pd.DataFrame(data_2, columns=["Channel Name", "Total Videos"], index=range(1, len(data_2) + 1))
            st.dataframe(df_1)
            st.success("DONE")



    # 3
    elif option == "What are the top 10 most viewed videos and their respective channels ?":
        if st.button("GET SOLUTION"):
            client=mysql.connector.connect(host="localhost",
                               user="root",
                               password="root",
                               database="proj_dsa")
            cursor=client.cursor()

            query_3 = """select channel.channel_name, video.video_name from channel inner join playlist on channel.channel_id=playlist.channel_id 
                         inner join video on playlist.playlist_id=video.playlist_id  order by view_count desc limit 10"""
            cursor.execute(query_3)
            data_3 = [i for i in cursor.fetchall()]
            df_3 = pd.DataFrame(data_3, columns=['Channels', 'Video Title'], index=range(1, len(data_3) + 1))
            st.dataframe(df_3)
            st.success("DONE")
            

# 4
    elif option == "How many comments were made on each video, and what are their corresponding video names?":
        if st.button("GET SOLUTION"):
            client=mysql.connector.connect(host="localhost",
                               user="root",
                               password="root",
                               database="proj_dsa")
            cursor=client.cursor()

            query_4 = "select video_name ,comment_count from video  order by comment_count desc"
            cursor.execute(query_4)
            data_4 = [i for i in cursor.fetchall()]
            st.dataframe(pd.DataFrame(data_4, columns=["Video Title", "Total Comments"], index=range(1, len(data_4) + 1)))
            st.success("DONE")
            
# 5
    elif option ==  "Which videos have the highest number of likes, and what are their corresponding channel names?":
        if st.button("GET SOLUTION"):
            client=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="proj_dsa")
            cursor=client.cursor()
            query_5 = """select channel.channel_name , video.video_name  from channel inner join playlist on channel.channel_id=playlist.channel_id 
                               inner join video on playlist.playlist_id=video.playlist_id order by like_count desc limit 1"""
            cursor.execute(query_5)
            data_5 = [i for i in cursor.fetchall()]
            st.dataframe(pd.DataFrame(data_5, columns=["Channel Names", "Video Title"], index=range(1, len(data_5) + 1)))
            st.success("DONE")
            
# 6
    elif option == "What is the total number of likes for each video, and what are  their corresponding video names?":
        if st.button("GET SOLUTION"):
            client=mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="root",
                                           database="proj_dsa")
            cursor=client.cursor()

            query_6 = "select video_name  , like_count  from video  order by like_count desc "
            cursor.execute(query_6)
            data_6 = [i for i in cursor.fetchall()]
            st.dataframe(pd.DataFrame(data_6, columns=["Title", "Likes", "Dislikes"], index=range(1, len(data_6) + 1)))
            st.success("DONE")
            cursor.close()
# 7
    elif option == "What is the total number of views for each channel, and what are their corresponding channel names?":
            if st.button("GET SOLUTION"):
                client=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="proj_dsa")
                cursor=client.cursor()

                query_7 = "select channel_name  , channel_views  from channel order by channel_views desc"
                cursor.execute(query_7)
                data_7 = [i for i in cursor.fetchall()]
                st.dataframe(pd.DataFrame(data_7, columns=["Channel Names", "Channel Views"], index=range(1, len(data_7) + 1)))
                st.success("DONE")
                
# 8
    elif option == "What are the names of all the channels that have published videos in the year 2022?":
            if st.button("GET SOLUTION"):
                client=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="proj_dsa")
                cursor=client.cursor()

                query_8 = """select channel.channel_name , video.year   from channel inner join playlist on channel.channel_id=playlist.channel_id 
                             inner join video on playlist.playlist_id=video.playlist_id where year = 2022 order by channel_name"""
                cursor.execute(query_8)
                data_8 = [i for i in cursor.fetchall()]
                st.code(f"Index   Channels  Year    ")
                st.code(pd.DataFrame(data_8, columns=["", ""], index=range(1, len(data_8) + 1)))
                st.success("DONE")
                
# 9
    elif option == "What is the average duration of all videos in each channel, and what are their corresponding channel names?":
            if st.button("GET SOLUTION"):
                client=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="proj_dsa")
                cursor=client.cursor()

                query_9 = """select channel.channel_name  , avg(video.duration)  from channel inner join playlist on channel.channel_id=playlist.channel_id 
                             inner join video on playlist.playlist_id=video.playlist_id group by channel_name order by avg(duration) desc"""
                cursor.execute(query_9)
                data_9 = [i for i in cursor.fetchall()]
                st.dataframe(pd.DataFrame(data_9, columns=["Channel Names", "Average Video Duration In Seconds"], index=range(1, len(data_9) + 1)))
                st.success("DONE")
                
# 10
    elif option == "Which videos have the highest number of comments, and what are their corresponding channel names?":
            if st.button("GET SOLUTION"):
                client=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="root",
                                   database="proj_dsa")
                cursor=client.cursor()

                query_10 = """select channel.channel_name , video.video_name from channel inner join playlist on channel.channel_id=playlist.channel_id 
                              inner join video on playlist.playlist_id=video.playlist_id order by comment_count desc limit 100"""
                cursor.execute(query_10)
                data_10 = [i for i in cursor.fetchall()]
                st.dataframe(pd.DataFrame(data_10, columns=["Channel Names", "Video Title"], index=range(1, len(data_10) + 1)))
                st.success("DONE")
                

    if st.button("clear database"):
        client=mysql.connector.connect(host="localhost",
                                       user="root",
                                       password="root",
                                       database="proj_dsa")
        cursor=client.cursor()
        cursor.execute("delete from comment")
        client.commit()
        cursor.execute("delete from video")
        client.commit()
        cursor.execute("delete from playlist")
        client.commit()
        cursor.execute("delete from channel")
        client.commit()
