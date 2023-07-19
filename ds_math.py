
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''------------------------------------------------------------'''
'''-----------------    Linear Functions   --------------------'''
'''------------------------------------------------------------'''

# A linear function has one independent variable (x) and one
#  dependent variable (y), and has the following form:

# y = f(x) = ax + b
# This function is used to calculate a value for the dependent
#  variable when we choose a value for the independent variable.

# Explanation:

# f(x) = the output (the dependant variable)
# x = the input (the independant variable)
# a = slope = is the coefficient of the independent variable.
#  It gives the rate of change of the dependent variable
# b = intercept = is the value of the dependent variable when x = 0.
#  It is also the point where the diagonal line crosses the vertical
#  axis.


'''------------------------------------------------------------'''
'''-----------------   Plotting Functions  --------------------'''
'''------------------------------------------------------------'''

# health_data = pd.read_csv('data.csv', header = 0, sep = ",")

# health_data.plot(x = 'Average_Pulse', y ='Calorie_Burnage')
# plt.ylim(ymin=0)
# plt.xlim(xmin=0)

# plt.show()

health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)

plt.show()

'''------------------------------------------------------------'''
'''-----------------   Slope and Intercept --------------------'''
'''------------------------------------------------------------'''

# calculate slope
def slope(x1,y1,x2,y2):
    s = (y2-y1)/(x2-x1)
    return s

print(slope(80,240,90,260)) # 2.0



# np.polyfit()
health_data = pd.read_csv("data.csv", header=0, sep=",")

x = health_data["Average_Pulse"]
y = health_data["Calorie_Burnage"]

slope_intercept = np.polyfit(x,y,1)
# The last parameter of the function specifies the degree
#  of the function, which in this case is "1".

print(slope_intercept)

# linear functions = 1.degree function. In our example,
#  the function is linear, which is in the 1.degree.
#  That means that all coefficients (the numbers) are
#  in the power of one.