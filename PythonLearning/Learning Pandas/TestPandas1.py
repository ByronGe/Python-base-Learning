import pandas as pd
import numpy as np
s=pd.Series([1,3,6])
print(s)
dates = pd.date_range('20170901',periods=3)
print(dates)
df = pd.DataFrame(np.random.randn(3,4),index=dates,columns=['a','b','c','d'])
print(df)
print(df.columns)
print(df.values)
print('-------------------')
print(df.describe())
print('-------------------')
print(df.T)
print(df.sort_index(axis=1,ascending=False))
print(df.sort_index(axis=0,ascending=False))
print(df.sort_values(by='b',ascending=False))