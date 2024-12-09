import pandas as pd
import numpy as np



data_sales=pd.read_csv('sales_col.csv',sep=',',index_col='Date',parse_dates=['Date'])

data_sales.head(5)
print(data_sales.head(5))
#data processing 
print(data_sales['Qty'].sum())
print('Null values in data set is',data_sales.isna().sum())


#data processing 