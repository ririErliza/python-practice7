import pandas as pd
import numpy as np

certificates_earned = pd.Series(
    [8, 2, 5, 6],
    index=['Tom', 'Kris', 'Ahmad', 'Beau']
)

print(certificates_earned)

#-----------------------

certificates_earned = pd.Series(
    [8, 2, 5, 6],
    index=['Tom', 'Kris', 'Ahmad', 'Beau']
)

print(certificates_earned[certificates_earned > 5])

#--------------------

certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})

certificates_earned.index = ['Tom', 'Kris', 'Ahmad', 'Beau']

print(certificates_earned.iloc[2]) #index location

#--------------------------
print('-----------------------')



print('---------long streak-----------')

certificates_earned = pd.DataFrame({
    'Certificates': [8, 2, 5, 6],
    'Time (in months)': [16, 5, 9, 12]
})
names = ['Tom', 'Kris', 'Ahmad', 'Beau']

certificates_earned.index = names
longest_streak = pd.Series([13, 11, 9, 7], index=names)
certificates_earned['Longest streak'] = longest_streak

print(certificates_earned)



print('---------cleaning-----------')
s = pd.Series(['a', 3, np.nan, 1, np.nan])

print(s.notnull().sum())



s = pd.Series([np.nan, 1, 2, np.nan, 3])
s = s.fillna(method='ffill')

print(s)
##########################################

a = np.array(([1,2,3,4,5], [6,7,8,9,10]))
b = np.max(a, axis=1)

print("b: ", b.sum())

######################################

a = np.ones((2,4))
print(a)
b = a.reshape((4,2))
print(b)

#####################################

filedata = np.genfromtxt('data.txt', delimiter=',')
output = np.any(filedata<50)
print("output any: ", output)
# output any:  True

output = np.all(filedata<50, axis = 1)
print("output all: ", output)
# output all:  [False False]

output = filedata[filedata<50]
print(output)
# [29. 32. 45. 15.  5. 22.]

