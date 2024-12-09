import pandas as pd
import numpy as np
import matplotlib.pylab as plt

#Data Pre Processing 
data_sales=pd.read_csv('Project_Ref/sales_col.csv',sep=',',index_col='Date',parse_dates=['Date'])

data_sales.head(5)
print(data_sales.head(5))
#data processing 
print(data_sales['Qty'].sum())
print('Null values in data set is',data_sales.isna().sum())


#Data Viualization 
pivot_data=pd.pivot_table(data_sales,values='Qty',index='Date',
                          columns='Date',aggfunc="sum")

print(pivot_data)