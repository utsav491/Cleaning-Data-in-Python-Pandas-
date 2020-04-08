# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 08:22:15 2020

@author: utsav
"""


import pandas as pd
import matplotlib.pyplot as plt
import os
files = os.listdir("E:\\Practice\\Pandas-Data-Science-Tasks-master\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data")
print(files)

concatenated_df = pd.DataFrame()
for file in files:
    df = pd.read_csv("E:\\Practice\\Pandas-Data-Science-Tasks-master\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data" + "\\" + file)
    concatenated_df = pd.concat([concatenated_df , df], axis =0)
print(concatenated_df)
concatenated_df.columns


concatenated_df.to_csv("all_months.csv", index = False)

all_month_df = pd.read_csv("E:\\Practice\\all_months.csv")
print(all_month_df)
 
""" What was the best month of the sales and how much money was earned in that month """

print(all_month_df.head())

all_month_df.columns
all_month_df.isnull().sum()
all_month_df.isnull().sum().plot(kind = 'bar')
all_month_df = all_month_df.dropna(how = "all")
all_month_df.shape

all_month_df["Month"] = all_month_df["Order Date"].str[0:2]
all_month_df["Month"].value_counts(ascending = True)
