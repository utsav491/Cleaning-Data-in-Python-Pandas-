# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 22:11:01 2019

@author: utsav
"""

# Import pandas
import pandas as pd
# Read the file into a DataFrame: df
df = pd.read_csv('C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Cleaning Data in Python\\dob_job_application_filings_subset.csv ')
h = df["Borough"]
i=list(h)
print(i)
g = df["Street Name"].str[0]

print(g.head())
df["Country"] = "USA"
# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Print the info of df
print(df.info())


c = df.describe()
print(c)



import operator

block_1 = df[operator.and_(df["Borough"] == "QUEENS" , df["Block"] < 1000)]
print(block_1) 
block_n = df[operator.and_(df["State"] == "CA" ,df["Lot"] < 1000)]
print(block_n)

block = df[(df["Block"]>500) & (df["Block"] < 1000)]  
print(block)

block  = df[(df["Block"] > 100) & (df["Block"] < 2000)]["Borough"]
print(block.head())

#Frequency Count

# Print the value_counts for 'Borough'
block_2 = df["Borough"].value_counts()
print(block_2)

df["City"]

# Print the value_counts for 'State'
block_3 = df["State"].value_counts(dropna = False)
print(block_3)

# Print the value counts for 'Job Type'
block_4 = df["Job Type"].value_counts(dropna = False).head()

# Print the value counts for 'Site Fill'
block_4 = df["Site Fill"].value_counts(dropna = False)
print(block_4)


# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create the boxplot
df.boxplot(column="initial_cost", by= "Borough", rot=90)

# Display the plot
plt.show()





# Import matplotlib.pyplot
import matplotlib.pyplot as plt
# Describe the column
df['Existing Zoning Sqft'].describe()
print(df['Existing Zoning Sqft'])
# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()





# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create the boxplot
df = pd.read_csv('C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Cleaning Data in Python\\dob_job_application_filings_subset.csv')

df.boxplot(column='initial_cost', by='Borough', rot=90)

# Display the plot
plt.show()
plt.clf()




# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Cleaning Data in Python\\dob_job_application_filings_subset.csv')
df["Initial Cost"] = df["Initial Cost"].str.replace("$","")
df["Total Est. Fee"] = df["Total Est. Fee"].str.replace("$","")

df["Initial Cost"] = pd.to_numeric(df["Initial Cost"])
df["Total Est. Fee"] = pd.to_numeric(df["Total Est. Fee"])


# Create and display the first scatter plot
df.plot(kind  = "scatter" ,x = "Initial Cost" ,y = "Total Est. Fee" , rot = 70)

plt.show()







#pd.melt(). There are two parameters you should be aware of: id_vars and value_vars.
# The id_vars represent the columns of the data you do not want to melt (i.e., keep it in its current shape),
# while the value_vars represent the columns you do wish to melt into rows.
# By default, if no value_vars are provided, all columns not set in the id_vars will be melted.
# This could save a bit of typing, depending on the number of columns that need to be melted.
import numpy as np
import pandas as pd 
df_air_quality = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Cleaning Data in Python\\airquality.csv")
print(df_air_quality.head())


df_air_quality_melt = pd.melt(df_air_quality, id_vars = ["Month" , "Day"] , value_vars= ["Ozone", "Wind"])
print(df_air_quality_melt.head())
print(df_air_quality_melt["variable"].value_counts())

df_air_quality_melt___ = pd.melt(df_air_quality,  id_vars = ["Month" , "Day" , "Ozone"],  value_vars =["Solar.R", "Wind"])
print(df_air_quality_melt___.head())
print(df_air_quality_melt___["variable"].unique())



# Melt df_air_quality: df_air_quality_melt
df_air_quality_melt_1 = pd.melt(df_air_quality, id_vars=['Month', 'Day'], var_name="measurement", value_name ="reading" )

# Print the head of df_air_quality_melt
print(df_air_quality_melt_1.head())

df_air_quality_melt_2 = df_air_quality.melt( id_vars = ["Month" , "Day"] , value_vars= ["Ozone", "Wind"])
print(df_air_quality_melt_2.head())

# Pivot df_air_quality_melt: df_air_quality_pivot
df_air_quality_pivot = pd.pivot_table( df_air_quality_melt_1,index = ["Month","Day"], columns = "measurement", values = "reading" )
print(df_air_quality_pivot)
print(df_air_quality_pivot.head())


# Pivot df_air_quality_melt: df_air_quality_pivot_1
df_air_quality_pivot_1 = df_air_quality_melt_1.pivot_table(index =["Month","Day"], columns = "measurement", values ="reading" )
print(df_air_quality_pivot_1)


# Print the index of airquality_pivot
print(df_air_quality_pivot_1.index)

# Reset the index of airquality_pivot: airquality_pivot_reset
df_air_quality_pivot_1_reset = df_air_quality_pivot_1.reset_index()

# Print the new index of airquality_pivot_reset
print(list(df_air_quality_pivot_1_reset.index))

# Print the head of airquality_pivot_reset
print(df_air_quality_pivot_1_reset.head())





#TB DataSet
# Import pandas
import pandas as pd
# Read the file into a DataFrame:TB
tb= pd.read_csv('C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Cleaning Data in Python\\tb.csv')
print(tb.head())
tb_melt = pd.melt(tb, id_vars= ["country", "year"])
print(tb_melt.head())

""" Capturing the first element of the string of a column insise a data frame """
tb_melt["Gender"] = tb_melt["variable"].str[0]
print(tb_melt["Gender"].value_counts())


tb_melt["Age Group"] = tb_melt["variable"].str[1:]
print(tb_melt["Age Group"].value_counts())
print(tb_melt["Age Group"].unique())


print(tb_melt.head())

print(tb_melt)



#Ebola DataSet
# Import pandas
import pandas as pd
# Read the file into a DataFrame: ebola
ebola = pd.read_csv('C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Cleaning Data in Python\\ebola.csv')
print(ebola.head())
print(ebola.columns)

ebola_melt = pd.melt(ebola, id_vars = ["Date" ,"Day"] , var_name ="type_country" , value_name = "counts" )
print(ebola_melt.head())

ebola_melt["str_split"] = ebola_melt["type_country"].str.split('_')
print(ebola_melt["str_split"])

ebola_melt["type"] = ebola_melt["str_split"].str.get(0)
print(ebola_melt["type"].head())

ebola_melt["Country"] = ebola_melt["str_split"].str.get(1)
print(ebola_melt["Country"].value_counts())



# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt, status_country], axis = 1)
print(ebola_tidy)
# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_tidy.head())






# NYC  Uber DataSet

import pandas as pd
pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Cleaning Data in Python\\nyc_uber_2014.csv")
# Concatenate uber1, uber2, and uber3: row_concat
row_concat = pd.concat([uber1,uber2,uber3])

# Print the shape of row_concat
print(row_concat.shape)

# Print the head of row_concat
print(row_concat.head())








# 1-1 Merge in Pandas
dict_1 = {
        "City": ["New York","LA","San Jose","Washington","Orlando","Miami"]
        ,"Temperature" : [90,21,22,34,75,59]
        , "rain":[12,3,4,4,66,98]
        }
df_1 = pd.DataFrame(dict_1)
print(df_1)
dict_2 = {
        "City" : ["New York","LA","Orlando","Miami","Oregan","Las Vegas"],
        "Humidity": [33,76,87,98,81,17]
        ,"snow":[3,45,677,788,99,80]
        }
df_2 = pd.DataFrame(dict_2)
print(df_2)


outer_merge_which_is_union_in_sets = pd.merge(left = df_1 , right = df_2 ,on = "City",how = "outer")
print(outer_merge_which_is_union_in_sets)

inner_merge_which_is_intersection_in_sets = pd.merge(left= df_1, right = df_2 , on ="City",how ="inner")
print(inner_merge_which_is_intersection_in_sets)

left_join_takes_all_the_elements_of_the_left_dataframe = pd.merge(left = df_1 , right = df_2  , how = "left",indicator = True)
print(left_join_takes_all_the_elements_of_the_left_dataframe)


left_join_takes_all_the_elements_of_the_left_dataframe_on = pd.merge(left = df_1 , right = df_2  ,on ="City", how = "left",indicator = True)
print(left_join_takes_all_the_elements_of_the_left_dataframe_on)

right_join_takes_all_the_elements_of_the_right_dataframe = pd.merge(left = df_1 , right = df_2 , on = "City" , how = "right")
print(right_join_takes_all_the_elements_of_the_right_dataframe)

indicator_in_merge_tells_us_where_the_element_came_from = pd.merge(left = df_1 , right = df_2 , on = "City" , how = "outer" , indicator = True)
print(indicator_in_merge_tells_us_where_the_element_came_from)



df_3 = pd.DataFrame(
                     {
                      "City" : ["new york","chicago", "DC"],
                      "temperature" :[2,3,54],
                      "humidity": [32,42,28]
                     })
print(df_3)

df_4 = pd.DataFrame(
                     {
                        "City": ["new york","DC","boston"]
                        ,"temperature" : [2,86,91]
                        ,"humidity" : [40,97,71]
                             })
print(df_4)

d = pd.merge(left= df_3 , right = df_4  , left_on = "City"  , right_on = "City" , how ="outer")
print(d)


e = pd.merge(left= df_3 , right = df_4  , left_on = "City"  , right_on = "City" , how ="inner")
print(e)

suffixes_in_the_merge = pd.merge(left = df_3 , right = df_4 , on = "City" , suffixes =(" on the left side"  , " on the right side" ) )
print(suffixes_in_the_merge)





#concat and merge DataFrames
import pandas as pd
raw_data_1 = pd.DataFrame({ "Member_id":[1,2,3,4,5],
                        "First_Name":["Adam", "Adrian", "Allan","Alexander","Andrew"],
                        "Last_Name":["Abraham","Allan","Allosp","Anderson","Arnold"]
        })
print(raw_data_1)

raw_data_2 =pd.DataFrame({"Member_id":[4,5,6,7,8],
                         "First_Name":["benjamin","blake", "borin","brandon","blake"]
                         ,"Last_Name":["baker" ,"ball", "bell","berry","black"]
                         })
print(raw_data_2)

#Row wise Concatination
row_wise_concatination = pd.concat([raw_data_1,raw_data_2] , axis = 0 )# axis = 0 ,concats the rows
print(row_wise_concatination)

#Column wise Conactination
column_wise_concatination = pd.concat([raw_data_1,raw_data_2] , axis = 1) #axis = 1 , concats the columns
print(column_wise_concatination)


#Merge Data Frame
#Inner Join
inner_join_merge = pd.merge( left = raw_data_1 , right = raw_data_2 , on = "Member_id" , how = "inner")
print(inner_join_merge)

#Outer Join
outer_join_merge = pd.merge(left = raw_data_1, right =  raw_data_2 , on ="Member_id" , how = "outer")
print(outer_join_merge)







import pandas as pd
df_5 = pd.DataFrame({
                        'lkey': ['foo', 'bar', 'baz', 'foo'],
                        'value': [1, 2, 3, 5],
                        "answer" : [3,4,5,6]
            }
                   )

df_6 = pd.DataFrame({
                            'rkey': ['foo', 'bar', 'baz', 'foo'],
                            'value': [5, 6, 7, 8],
                            "answer": [4,3,3,9]
                    })


v = pd.merge(left = df_5 ,right  = df_6  ,on = "value", how = "left")
print(v)

import pandas as pd
df_7 = pd.DataFrame({"HPI" :[80,85,88,85],
                     "Int_Rate": [2,3,2,2],
                     "US_GDP_Thousands": [50,55,65,55],
                     },index = [2001,2002,2003,2004])

print(df_7)
df_8 = pd.DataFrame(
                     {
                      "HPI" :[80,85,88,85],
                      "Int_Rate": [2,3,2,2],
                      "US_GDP_Thousands": [50,55,65,55],
                     },index = [2005,2006,2007,2008])

print(df_8)

print(df_8["HPI"][2006])

f = pd.merge(left = df_7, right = df_8, on = "HPI" , how = "outer", indicator = False)
print(f)
df_9 = pd.DataFrame(
                     {
                      "HPI" :[80,85,88,85],
                      "Unemployment": [7,8,9,6],
                      "Low_tier_HPI": [50,52,50,53],
                     },index = [2001,2002,2003,2004])








#Tips DataSet
import pandas as pd
tips_df = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Cleaning Data in Python\\tips.csv")
print(tips_df.head())
print(tips_df.info())
# Convert the sex column to type 'category'

tips_df["sex"] = tips_df["sex"].astype("category")
print(tips_df.info())

# Convert the smoker column to type 'category'
tips_df["smoker"] = tips_df["smoker"].astype("category")
print(tips_df.info())


# Convert 'total_bill' to a numeric dtype
tips_df["total_bill"] = pd.to_numeric(tips_df["total_bill"] , errors = "coerce" )
print(tips_df.info())


# Convert 'tip' to a numeric dtype
tips_df["tip"] = pd.to_numeric(tips_df["tip"] , errors = "coerce")
print(tips_df.info())






# Import the regular expression module
import re
# Compile the pattern: prog
prog = re.compile('\d{3}-\d{3}-\d{4}')

# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))

# See if the pattern matches
result2 = prog.match("1123 - 456 - 7890")
print(bool(result2))



a = re.compile('\d* ')
result = a.match("17")
print(bool(result))



b = re.compile('\$\d*')
result_b = b.match("$18")
print(bool(result_b))


c = re.compile("\$\d*\.\d")
result_c = c.match("$19.00")
print(bool(result_c))


e = re.compile("^\$\d*\.\d{3}$")
result_e = e.match("$19.495")
print(bool(result_e))


f = re.compile("\$\d*\.\d{2}")
result_f = f.match("$19.96")
print(bool(result_f))


g = re.compile("\$\d*\.\d{3}")
result_g = g.match("$10.987")
print(bool(result_g))





import re 

cd = re.findall('\d+', "the statement has the number 10 ,it has 4 and it also has 33")
print(cd)


# Find the numeric values: matches
matches = re.findall('\d+ ', 'the recipe calls for 10 strawberries and 1 banana')

# Print the matches
print(matches)





# Write the first pattern
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)

# Write the second pattern
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)

# Write the third pattern
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
print(pattern3)

"""fillna method in Pyhton"""
import pandas as pd
import numpy as np


df_fillna = pd.DataFrame(
                    [
                     [np.nan, 2, np.nan, 0],
                     [3, 4, np.nan, 1],
                     [np.nan, np.nan, np.nan, 5],
                     [np.nan, 3, np.nan, 4]
                     ], columns=list('ABCD')
                  )

print(df_fillna)

"""Replace all NaN elements with 0s"""
df_fillna.fillna(0)

"""We can also propagate non-null values forward or backward."""

"""Forward fill"""
df_fillna.fillna(method = "ffill")

"""Backward Fill"""
df_fillna.fillna(method = "bfill")



"""Replace all NaN elements in column ‘A’, ‘B’, ‘C’, and ‘D’, with 0, 1, 2, and 3 respectively"""
values = {"A":0 ,"B":1,"C":2, "D":3}
df_fillna.fillna(value = values)

"""Only replace the first NaN element."""
df_fillna.fillna(value=values, limit=1)
print(df_fillna)



""" dropna method in Python """
import pandas as pd
import numpy as np
df_dropna = pd.DataFrame(
                    {
                            "name": ['Alfred', 'Batman', 'Catwoman'],
                            "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                            "born": [pd.NaT, pd.Timestamp("1940-04-25") ,pd.NaT]
                    }
                )
print(df_dropna)
""" Drop the rows where at least one element is missing"""

values_are_dropped = df_dropna.dropna()
print(values_are_dropped)



"""Drop the columns where at least one element is missing."""
df_dropna.dropna(axis = "columns")


"""Drop the rows where all elements are missing"""
df_dropna.dropna(how = "all")


"""Keep only the rows with at least 2 non-NA values."""
df_dropna.dropna(thresh = 2)


"""Define in which columns to look for missing values."""
df_dropna.dropna(subset=['name', 'born'])
 

""""Keep the DataFrame with valid entries in the same variable"""
df_dropna.dropna(inplace = True)









# Create the new DataFrame: tracks
tracks = billboard[["year","artist","track","time"]]
print(tracks.head())
# Print info of tracks
print(tracks.info())

# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()

# Print info of tracks
print(tracks_no_duplicates.info())




#Removing the Duplicate values froom the DataSet

import pandas as pd 
df_air_quality = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Cleaning Data in Python\\airquality.csv")

#Creting a new DataFrame
tracks = df_air_quality[["Ozone" , "Wind" , "Temp" , "Solar.R"]]
print(tracks.head())

#Print info of tracks
print(tracks.info())

tracks_no_duplicates = tracks.drop_duplicates()

# Print info of tracks
print(tracks_no_duplicates.info())



"""# Calculate the mean of the Ozone column: oz_mean"""
oz_mean = df_air_quality["Ozone"].mean()
print(oz_mean)


"""# Replace all the missing values in the Ozone column with the mean"""
df_air_quality["Ozone"] = df_air_quality["Ozone"].fillna(oz_mean)
print(df_air_quality["Ozone"].head())


"""# Print the info of airquality"""
print(df_air_quality.info())
print(df_air_quality["Ozone"])



"""#calculate the mean of the Solar.R column :solar_mean"""
solar_mean = df_air_quality["Solar.R"].mean()
print(solar_mean)


"""#Replace all the missing values in the Solar.R column by the mean value of the column"""
df_air_quality["Solar.R"] = df_air_quality["Solar.R"].fillna(solar_mean)
print(df_air_quality.info())



""" assert method """

#Ebola DataSet
# Import pandas
import pandas as pd
# Read the file into a DataFrame: ebola
ebola = pd.read_csv('C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Cleaning Data in Python\\ebola.csv')
print(ebola)
# Assert that there are no missing values
assert pd.notnull(ebola).all().all()

# Assert that all values are >= 0
assert (ebola >= 0).all().all()




g1800s = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Cleaning Data in Python\\gapminder.csv")
print(g1800s)
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Create the scatter plot
g1800s.plot(kind='scatter', x='1800', y='1899')

# Specify axis labels
plt.xlabel('Life Expectancy in 1800')
plt.ylabel('Life Expectancy in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()



import pandas as pd
df = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Pandas\\austin_airport_departure_data_2015_july.csv" ,  skiprows = 12)



import pandas as pd
df_1 = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Pandas\\NOAA_QCLCD_2011_hourly_13904.txt",  header = None )
print(df_1)



import pandas as pd
# Create dataframe
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])
print(df.head())

group = df.groupby(["regiment"]).max()[["preTestScore", "company"]]
group
