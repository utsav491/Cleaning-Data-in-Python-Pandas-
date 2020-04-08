# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:15:00 2019

@author: utsav
"""

""" Using a Loop """

filename = ["a.csv" ,"b.csv"]

importing_multiple_files_through_loop = [pd.read_csv(f) for f in filename]


""" Importing Multiple Files """ 

# Create the list of file names: filenames
filenames = ['Gold.csv', 'Silver.csv', 'Bronze.csv']

# Create the list of three DataFrames: dataframes
dataframes = []
for filename in filenames:
    dataframes.append(pd.read_csv(filename))



"""Sorting DataFrame with the Index & columns"""


# Import pandas
import pandas as pd

# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Merging Data Frames in Pandas\\weather.csv", index_col = "Events")

# Print the head of weather1
print(weather1.head())

# Sort the index of weather1 in alphabetical order: weather2
weather2 = weather1.sort_index()

# Print the head of weather2
print(weather2.head())

# Sort the index of weather1 in reverse alphabetical order: weather3
weather3 = weather2.sort_index(ascending  = False)

# Print the head of weather3
print(weather3.head())

# Sort weather1 numerically using the values of 'Max TemperatureF': weather4
weather4 = weather1.sort_values('Max TemperatureF')

# Print the head of weather4
print(weather4.head())


weather5 = weather1.sort_values("Max TemperatureF" , ascending  = False)
print(weather5.head())    






# Import pandas
import pandas as pd

# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Merging Data Frames in Pandas\\weather.csv")
weather2 = weather1.iloc[0:6,:]
print(weather2)
weather2["month"] = ['Jan','Feb','Mar','Apr','May','Jun']
print(weather2)
weather2 = weather2.set_index("month")
print(weather2)
year = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

# Reindex weather1 using the list year: weather2
weather2 = weather2.reindex(year)
print(weather2)

# Reindex weather1 using the list year with forward-fill: weather3
weather3 = weather2.reindex(year,method = 'ffill')

# Print weather3
print(weather3)
# Print weather2
print(weather2)




"""Reindexing using another DataFrame Index"""

# Import pandas
import pandas as pd

# Reindex names_1981 with index of names_1881: common_names
common_names =names_1981.reindex(names_1881.index)

# Print shape of common_names
print(common_names.shape)

# Drop rows with null counts: common_names
common_names = common_names.dropna()

# Print shape of new common_names
print(common_names.shape)






"""Broadcasting in arithmetic formulas """

import pandas as pd

# Read 'monthly_max_temp.csv' into a DataFrame: weather1
weather1 = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Merging Data Frames in Pandas\\weather.csv")

# Extract selected columns from weather as new DataFrame: temps_f
temps_f = weather1[['Min TemperatureF', 'Mean TemperatureF', 'Max TemperatureF']]

print(temps_f)

# Convert temps_f to celsius: temps_c
temps_c = (temps_f - 32) * 5/9
print(temps_c)

# Rename 'F' in column names with 'C': temps_c.columns
temps_c.columns = temps_c.columns.str.replace("F", "C")

# Print first 5 rows of temps_c
print(temps_c.head())




"""Computing percentage growth of GDP"""



import pandas as pd

gdp = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Merging Data Frames in Pandas\\GDP\\gdp_usa.csv",index_col = "DATE" , parse_dates = True)
print(gdp.head())


# Slice all the gdp data from 2008 onward: post2008
post2008 = gdp.loc["2008 -01 -01": ]
print(post2008)


# Print the last 8 rows of post2008
print(post2008.tail(8))


# Resample post2008 by year, keeping last(): yearly
yearly = gdp.resample("A").last()
print(type(yearly))
print(yearly)


# Compute percentage growth of yearly: yearly['growth']
yearly["growth"] = yearly.pct_change() * 100 
print(yearly)




""" .multiply Function """

# Import pandas
import pandas as pd

# Read 'sp500.csv' into a DataFrame: sp500
sp500 = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Merging Data Frames in Pandas\\sp500.csv" , index_col = "Date" , parse_dates= True)
print(sp500.columns)


# Read 'exchange.csv' into a DataFrame: exchange
exchange = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Merging Data Frames in Pandas\\exchange.csv" , index_col = "Date", parse_dates = True)
print(exchange)


# Subset 'Open' & 'Close' columns from sp500: dollars
dollars = sp500[["Open" ,"Close"]]

# Convert dollars to pounds: pounds
pounds = dollars.multiply(exchange["GBP/USD"] , axis = "rows")

# Print the head of pounds
print(pounds.head())








"""Appending pandas Series"""



# Import pandas
import pandas as pd


# Load 'sales-jan-2015.csv' into a DataFrame: jan
jan = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Merging Data Frames in Pandas\\Sales\\sales-jan-2015.csv" , index_col = "Date" , parse_dates= True)
print(jan.shape)


# Load 'sales-feb-2015.csv' into a DataFrame: feb
feb = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Merging Data Frames in Pandas\\Sales\\sales-feb-2015.csv",index_col = "Date" ,parse_dates = True)
print(feb)


# Load 'sales-mar-2015.csv' into a DataFrame: mar
mar = pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Merging Data Frames in Pandas\\Sales\\sales-mar-2015.csv",index_col = "Date" ,parse_dates = True)
print(mar)


# Extract the 'Units' column from jan: jan_units
jan_units = jan["Units"]
print(jan_units)


# Extract the 'Units' column from feb: feb_units
feb_units = feb["Units"]
print(feb_units)


# Extract the 'Units' column from mar: mar_units
mar_units = mar["Units"]
print(mar_units.shape)


# Append feb_units and then mar_units to jan_units: quarter1

quarter1 = jan_units.append(feb_units).append(mar_units)
print(quarter1)


# Print the first slice from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])


# Print the second slice from quarter1
print(quarter1.loc["feb 26 ,2015":"mar 7,2015"])


# Compute & print total sales in quarter1
print(quarter1.sum())








"""Concatenating pandas Series along row axis"""

import pandas as pd

new_list= []

for x in jan, feb ,mar:
    new_list.append(x["Units"])

print(new_list)
    

quarter_row_1 = pd.concat(new_list )
print(quarter_row_1)


# Print slices from quarter1
print(quarter1.loc['jan 27, 2015':'feb 2, 2015'])
print(quarter1.loc['feb 26, 2015':'mar 7, 2015'])


#Convert to a DataFrame
df= pd.DataFrame(quarter_row_1)
print(type(df))




# Import pandas
import pandas as pd


# Load 'names1881.csv' into a DataFrame: jan
name = ["Name" , "Gender" , "Number"]
names_1881= pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Merging Data Frames in Pandas\\Baby names\\names1881.csv" , header = None , names = name)
print(names_1881.head())


# Load 'names1981.csv' into a DataFrame: jan
names_1981= pd.read_csv("C:\\Users\\utsav\\Desktop\\Python_Data_Sets_Data_Camp\\Merging Data Frames in Pandas\\Baby names\\names1981.csv" , header = None , names = name)
print(names_1981.head())


# Add 'year' column to names_1881 and names_1981
names_1881['year'] = 1881
names_1981['year'] = 1981



# Append names_1981 after names_1881 with ignore_index=True: combined_names
combined_names = names_1881.append(names_1981, ignore_index= True)

# Print shapes of names_1981, names_1881, and combined_names
print(names_1981.shape)
print(names_1881.shape)
print(combined_names.shape)


# Print all rows that contain the name 'Morgan'
print(combined_names[combined_names["Name"] == "Morgan"])






""" Merge DF """


import pandas as pd

revenue = pd.DataFrame({
          "city":["Austin" , "Denver" , "Springfield" ,"Mendocino"],
           "branch_id" :[10,20,31,47] ,
            "revenue" :[100,83,4,200]  ,           
})



managers = pd.DataFrame({"city" :["Austin" ,"Denver" ,"Mendocino" ,"Springfield"],
                         "branch_id" :[10,20,47,30],
                         "manager":["Charles" , "Joel" ,"Brett", "Sally"]
                         })

    
print(revenue , managers)

merge_by_city = pd.merge(left  = revenue, right  = managers  ,on = "city")
print(merge_by_city)


# Merge revenue & managers on 'city' & 'branch': combined
combined = pd.merge(left = revenue , right = managers , left_on = "city" , right_on = "city")

# Print combined
print(combined)



# Add 'state' column to revenue: revenue['state']
revenue['state'] = ['TX','CO','IL','CA']

# Add 'state' column to managers: managers['state']
managers['state'] = ['TX','CO','CA','MO']
print(revenue ,"\n", managers)

# Merge revenue & managers on 'branch_id', 'city', & 'state': combined
combined = pd.merge(revenue, managers , on =["branch_id" ,"city" , "state"] )

# Print combined
print(combined)




import pandas as pd

revenue =pd.DataFrame({"city" :["Austin" ,"Denver" ,"Mendocino" ,"Springfield"],
                       "state" :["TX", "CO","IL","MO"],
                       "branch_id" :[10,20,30,47],
                       "revenue" :[100,83,4,200]
                       })

    
sales = pd.DataFrame({
                        "city" :["Austin" ,"Denver" ,"Mendocino" ,"Springfield","Springfield"],
                        "state" :[ "TX" , "CO" ,"IL" , "MO" , "IL" ] 
                        ,"units":[1,4,2,5,1]
                        })


    
    
managers = pd.DataFrame({"branch" :["Austin" ,"Denver" ,"Mendocino" ,"Springfield"],
                         "branch_id" :[10,20,47,30],
                         "manager":["Charles" , "Joel" ,"Brett", "Sally"] ,
                         "state" :["TX" ,"CO","IL", "MO"]
                         })

print(revenue)
print(sales)
print(managers)    


revenue_and_sales = pd.merge( left  = revenue , right = sales  ,on =["city" ,"state"]  ,how = "left")
print(revenue_and_sales)

revenue_and_sales = pd.merge( left  = revenue , right = sales  ,on =["city" ,"state"]  ,how = "right")
print(revenue_and_sales)

sales_and_managers = pd.merge(left =  sales , right = managers , right_on =["branch" , "state"] , left_on = ["city","state" ] )
print(sales_and_managers)


# Perform the first merge: merge_default
merge_default = pd.merge(sales_and_managers , revenue_and_sales)

# Print merge_default
print(merge_default)

# Perform the second merge: merge_outer
merge_outer = pd.merge(sales_and_managers , revenue_and_sales, how ="outer" )

# Print merge_outer
print(merge_outer)

# Perform the third merge: merge_outer_on
merge_outer_on = pd.merge(sales_and_managers , revenue_and_sales , on = ["city" , "state"], how = "outer")

# Print merge_outer_on
print(merge_outer_on)



austin = pd.DataFrame({"date" : ["2018 -01-01" ,"2018 - 01 -15", "2018 -09 -01" ] , 
                       "weather": ["Rainy", "Rainy", "Cloudy"]
                       })

houston = pd.DataFrame({"date" : ["2018 -01-01" ,"2018 - 03 -05", "2018 -10 -21" ] , 
                       "weather": ["Rainy", "Cloudy", "Cloudy"]
                       })
    
# Perform the first ordered merge: tx_weather
tx_weather = pd.merge_ordered(austin ,houston)

# Print tx_weather
print(tx_weather)

# Perform the second ordered merge: tx_weather_suff
tx_weather_suff = pd.merge_ordered(austin ,houston ,on ="date" ,suffixes = ["_aus", "_hus"])

# Print tx_weather_suff
print(tx_weather_suff)

# Perform the third ordered merge: tx_weather_ffill
tx_weather_ffill = pd.merge_ordered(austin, houston , on ="date", suffixes = ["_aus", "_hus"], fill_method="ffill")

# Print tx_weather_ffill
print(tx_weather_ffill)












""" VERY IMPORTANT EXAMPLE """

import pandas as pd

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})


right = pd.DataFrame({
                     'key1': ['K0', 'K1', 'K1', 'K2'],
                     'key2': ['K0', 'K0', 'K0', 'K0'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']
                     })

print(left)
print(right)
print(left["key1"])
result = pd.merge(left, right, on=['key1', 'key2'])

print(result)



result_1 = pd.merge(left, right, how='left', on=['key1', 'key2'])
print(result_1)


result_2 = pd.merge(left, right, how='right', on=['key1', 'key2'])
print(result_2)


result_3 = pd.merge(left, right, how='outer', on=['key1', 'key2'])
print(result_3)



result_4 = pd.merge(left, right, how='inner', on=['key1', 'key2'])
print(result_4)

