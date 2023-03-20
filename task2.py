import pandas as pd

df1 = pd.read_excel('Test_02_07_2021.xlsm')
df2 = pd.read_excel('Test_02_08_2021.xlsm')

#find the difference between the two files
difference_df1 = df1[df1!=df2]
difference_df2 = df2[df2!=df1]
print("Values in DF1, not in DF2: ",difference_df1)
print(difference_df2)

#find the largest date range from start to end (or current date)
from datetime import date
today = date.today()
df3 = pd.concat([df1,df1], ignore_index=True)
df3['EndDate'] = df3['EndDate'].fillna(value=today)
end = df3['EndDate'].values.tolist()
start = df3['StartDate'].values.tolist()
difflist = end - start
print("Largest date range is " + max(difflist))