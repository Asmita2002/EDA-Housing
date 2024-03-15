# EDA-Housing
Exploratory Data Analysis project on Housing Prices in Alberta, Canada.

## Alberta Housing Market - Data Analysis
This project aims to predict housing prices in Alberta, Canada, based on exploratory data analysis (EDA) and predictive analysis. The dataset used in this project was obtained from Kaggle and contains information about various housing features such as the number of bedrooms, bathrooms, square footage of property and locality information.

## Exploratory Data Analysis (EDA)
The EDA phase explores the dataset to gain insights into the distribution and relationships between different housing features, and explores data patterns through data cleaning process and feature engineering. 
Techniques such as data visualization and statistical analysis were used to understand the characteristics of the data.

## Predictive Analysis - Regression Models
Predictive analysis was performed to develop models that can accurately predict housing prices based on the available features such as num_beds, num_baths, sq_ft, place.

Place, being a categorical variable was converted to numerical using Binary Encoding
Machine learning techniques were employed, and different models were trained and evaluated using libraries such as Scikit-learn. 
Since the housing data features are not exactly linear, Random Forest Regression performs better in predicting housing prices. 

## Libraries
Pandas: Data manipulation and analysis.

Matplotlib: Data visualization.

Scikit-learn: Machine learning models and evaluation.

XGBoost: Gradient boosting implementation for predictive modeling.

