# Installing neccessary packages, all might not be needed, depends on what we find
%pip install klib
%pip install sketch
%pip install h5py
%pip install typing-extensions
%pip install wheel
%pip install dataprep
%pip install -U dataprep
%pip install markupsafe==2.0.1
%pip install Cmake
%pip install plotly==5.18.0

 %pip install black
 %pip install click.core
 %pip install --upgrade Jinja2
 %pip install dataprep.eda
 pip install -U click

pip show pandas


# Step 0

# Loading our packages 

import pandas as pd #importing pandas libraries for analysis (data processing)
import numpy as np #numpy libraries for analysis (linear algebra)
import plotly.express as px
import klib 
import matplotlib.pylab as plt #visualization
import seaborn as sns #for exploratory plots
from matplotlib import *
from dataprep.eda import plot
pd.set_option('display.max_columns', 50)
%matplotlib inline
from encodings.aliases import aliases 
plt.style.use('ggplot')


# Importing our dataframe
df = pd.read_csv('shopping_behavior_and_trends.csv')


# Step 1
# Understanding our data

df.shape # handling a dataset with 3900 rows and 18 columns --> 70.000+ datapoints, hence displaying 20 columns is enough
df.info() # all column names with data types connected to the columns, majority of the datapoints consists of objects
df.columns #printing out column name, might need later for subsetting
df.head() #getting out the top 5 columns, good to be able to see the actual rows and columns. 
df.describe() #important stats about the numeric data in our data set, ignore Customer ID. Min and max age is 18 and 70, purchase amount 20 and 100, ratings go to 5 stars.


#Step 2

# Data preparation
# After we now understand what type of data we have, its columns and rows. It is time to clean our data.

df.head(20) #Checking if anything needs to be cleaned or if I won't be using some columns. 

################################## Conclusion: Data is pretty clean, but we need to change datatype of the 'review rating' column. Or else we can't make calculations
################################## df ['Review Rating'] = df['Review Rating'].astype(float)

###############display(df.dtypes) #Seeing that float data type does not exist anymore (doesn't work?)
###############df.head()

display(df.dtypes) # Doublechecking again and seeing that our columns have valid data types

# Renaming some columns to make them more obvious
# Changing:
# Location --> Purchase Location
# Color --> Item Color
# Size --> Item Size
# Category  --> Item Category

df.columns
df = df.rename(columns={'Category':'Item Category','Size':'Item Size','Color':'Item Color', 'Location':'Purchase Location'})
df.head()        

#Check if we have missing values in our dataset
df.isna().sum() #basically showing us no missing values, which is perfect

#Checking for duplications in our data
df.duplicated().sum() #no duplicates


# Step 3
# EDA, understand data and discover insights via data visualization, data summarization etc.
# Understanding distributions and potential outliers of our dataset
# Unvariate analysis
# Plotting Feature Distributions
# Histograms
# KDE
# Boxplots

# Unique values
df['Purchase Amount (USD)'].value_counts() #ordering from most to least occuring
ax = df['Purchase Amount (USD)'].value_counts().head(10).plot(kind='bar', title='Top 10 Purchasing amounts') #visualizing top 10 most common values in this column
ax.set_xlabel('Purchase Amount in USD')
ax.set_ylabel('Count')

# Get an idea of the distrubution of a column (add some more columns and historgrams here later)

df['Age'].plot(kind='hist',bins=20)
df['Purchase Amount (USD)'].plot(kind='hist',bins=20)
df['Review Rating'].plot(kind='hist',bins=20)
df['Previous Purchases'].plot(kind='hist',bins=20)


# Step 4

# The fun part, see if there is some relationships between the variables in the dataset, how the datapoints relate to eachother
# Scatterplots, to compare features side by side
# Heatmap correlation
# Pairplot
# Groupby comparisons

df.info()
df.plot(kind='scatter', x='Purchase Amount (USD)', y='Age', title='Purchase Amount vs. Age')
df.plot(kind='scatter', x='Purchase Amount (USD)', y='Previous Purchases', title='Purchase Amount vs. Previous purchases')
df.plot(kind='scatter', x='Previous Purchases', y='Age', title='Purchase Amount vs. Previous purchases', x_min=)
plt.show()

plot(df)