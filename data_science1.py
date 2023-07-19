import pandas as pd
import numpy as np

# intro to data science with python

'''------------------------------------------------------------'''
'''--------------------     DataFrame    ----------------------'''
'''------------------------------------------------------------'''

d = {
    'col1': [1,2,3,4,6],
    'col2': [4,5,6,9,5],
    'col3': [7,8,12,1,11]
    }

df = pd.DataFrame(data=d)
# print(df)

#    col1  col2  col3
# 0     1     4     7
# 1     2     5     8
# 2     3     6    12
# 3     4     9     1
# 4     6     5    11

count_column = df.shape[1]
print(count_column) # 3

count_row = df.shape[0]
print(count_row) # 5


'''------------------------------------------------------------'''
'''--------------------   DS Functions   ----------------------'''
'''------------------------------------------------------------'''

# max()
Average_pulse_max = max(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print(Average_pulse_max) # 125


# min()
Average_pulse_min = min(80, 85, 90, 95, 100, 105, 110, 115, 120, 125)
print (Average_pulse_min) # 80

# mean()
Calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]
Average_calorie_burnage = np.mean(Calorie_burnage)
print(Average_calorie_burnage)


'''------------------------------------------------------------'''
'''------------------   Data Preparation   --------------------'''
'''------------------------------------------------------------'''

health_data = pd.read_csv("data.csv", header=0, sep=",")
print(health_data)


# head() 
print(health_data.head()) # only showing top 5 rows

# dropna()
# remove blank rows
health_data.dropna(axis=0, inplace=True)
print(health_data)

# info()
print(health_data.info())
# Data columns (total 6 columns):
#  #   Column           Non-Null Count  Dtype
# ---  ------           --------------  -----
#  0   Duration         10 non-null     float64
#  1   Average_Pulse    10 non-null     object
#  2   Max_Pulse        10 non-null     object
#  3   Calorie_Burnage  10 non-null     float64
#  4   Hours_Work       10 non-null     float64
#  5   Hours_Sleep      10 non-null     float64
# dtypes: float64(4), object(2)
# memory usage: 560.0+ bytes
# None

# astype()
# convert the data

health_data["Average_Pulse"] = health_data["Average_Pulse"].astype(float)
health_data["Max_Pulse"] = health_data["Max_Pulse"].astype(float)

print (health_data.info())