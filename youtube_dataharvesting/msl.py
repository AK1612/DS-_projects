import mysql.connector
client=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)
cursor=client.cursor()
cursor.execute("create database project_youtube")
client=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="project_dsa"
)
cursor=client.cursor()
#table channel
query="""create table channel(channel_id varchar(255) primary key,
       channel_name varchar(255), channel_views int, channel_description text)"""
cursor.execute(query)
#table playlist
query="""create table playlist(playlist_id varchar(255) primary key,
       channel_id varchar(255), playlist_name varchar(255))"""
cursor.execute(query)
#table video
query="""create table video(video_id varchar(255) primary key,
       playlist_id varchar(255), video_name varchar(255), video_description text,
       view_count int,like_count int,favorite_count int,comment_count int,duration int,
       thumbnail varchar(255),published_date datetime, year int)"""
cursor.execute(query)
#table comment
query="""create table comment(comment_id varchar(255) primary key, video_id varchar(255) , comment text, comment_author varchar(255),
       comment_pub_date datetime)"""
cursor.execute(query)



