# **INDUSTRIAL COPPER MODELING**

![](https://www.livemint.com/lm-img/img/2024/02/04/600x338/KutchCopper_1707042921942_1707042922101.jpg)


> ## **Overview**

   This project aims to create a machine learning model for predicting the price of the copper and status of the leads 

   
# Approach 

  - Load Copper_Set.xlsx - Result 1.csv file into pandas DataFrame.
    
  - Clean and preprocess the data to remove outliers, skewness, less important features

  - Use plotly and seaborn for data visualisation

  - Convert catagorical into numerical data using one hot encoding

  - Train different regression models and compare the `MEAN ABSOLUTE ERROR, MEAN SQUARE ERROR AND R2 SCORE` values to select the best model for price prediction

  - Use grid search to find the best hyperparameters for selected model

  - Train the model multiple times using best hyperparameters and pickle the model

  - Train different classification models and compare the `Accuracy score, precission score and f1 score` values to select the best model for status prediction

  - Use grid search to find the best hyperparameters for selected model

  - Train the model multiple times using best hyperparameters and pickle the model
    
  - Implement Streamlit to create a user-friendly dashboard for price and status prediction.
    
   

# Getting Started

  - Install/Import the necessary modules: Streamlit, Pandas, sk learn, plotly and seaborn.
    

# Technical Steps to Execute the Project

### Step 1: Install/Import Modules

   - Ensure the required Python modules are installed: Streamlit, Pandas, sk learn, plotly and seaborn.

### Step 2: Write required codes to load and clean the data

   - In this step cover tasks like data cleaning and data analysis

### Step 3: Run the Project with Streamlit

   - Execute the command: streamlit run main.py. This will open a web browser, such as Google Chrome, displays the user interface.


# Tools Expertise 

   - Python
     
   - pandas
     
   - sk learn
     
   - plotly and seaborn
     
   - IDE: visual studio codes


  
