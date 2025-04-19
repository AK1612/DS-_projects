# YouTube Data Harvesting Warehousing and Data Analysis
![Image](https://github.com/user-attachments/assets/c47d7852-83a5-437a-9174-86abe01f6b55)
# Overview

 - This project is focused on harvesting data from YouTube channels using the YouTube API, processing the data, and warehousing it. The harvested data is stored in a SQL database for in-depth data analysis. The project's core functionality relies on the Extract, Transform, Load & process.

# Approach 
![image](https://github.com/user-attachments/assets/3a3e4454-b03c-429c-b3f8-c692d070ce8d)

 
# Getting Started

  - Install/Import the necessary modules: Streamlit, Pandas, MYSQL, Googleapiclient.
    
  - Ensure you have access to MYSQL and set up a SQL DBMS on your local environment.

# Technical Steps to Execute the Project

### Step 1: Install/Import Modules

   - Ensure the required Python modules are installed: MYSQL, Streamlit, Pandas, Googleapiclient, and Isodate.

### Step 2: Write required codes to extract, clean and store the data using youtube API

   - In this step cover tasks like data retrieval, data storage, and data analysis

### Step 3: Run the Project with Streamlit

   - Open the command prompt in the directory where "youtube_project_1.py" is located.
   - Execute the command: streamlit run youtube_project_1.py. This will open a web browser, such as Google Chrome, displaying the project's user interface.

### Step 4: Configure Databases

   - Ensure that you are connected to MYSQL DBMS.

# Methods

   - Get YouTube Channel Data: Fetches YouTube channel data using a Channel ID and creates channel details in list format.
     
   - Get Playlist Videos: Retrieves all playlist IDs for a provided channel ID.
     
   - Get Video: Returns video details for the given playlist IDs
    
   - Comment Details: returns comment details for the given video IDs.
     
   - Get All Channel Details: Provides channel, video, comment and playlist details in list format.
     
   - Insert Data into SQL DB: Inserts channel data into SQL DB.
     
   - Data Analysis: Conducts data analysis using SQL queries and Python integration.
     
   - Delete SQL Records: Deletes SQL records related to the provided YouTube channel data with various options.

# Tools Expertise 

   - Python
     
   - SQL
     
   - API Integration
     
   - Data Management using MYSQL
     
   - IDE: visual studio codes

# Result :

   - This project focuses on harvesting YouTube data using the YouTube API, storing it in SQL DB for analysis. Utilizes Streamlit and Python. Expertise includes Python, SQL, API integration . This project mainly aims to make interface for analysing the youtue data by pasting the channnel id and some clicks
