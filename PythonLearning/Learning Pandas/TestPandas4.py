import pandas as pd
import numpy as np

dates = pd.date_range('20170901',periods=4)
df = pd.DataFrame(np.arange(16).reshape(4,4),index=dates,columns=['a','b','c','d'])
df.iloc[0,1]=np.nan
df.iloc[2,3]=np.nan
print(df)
#print(df.dropna(axis=1,how='any'))
print(df.isnull())
print(np.any(df.isnull())==True)