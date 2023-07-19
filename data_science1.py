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
