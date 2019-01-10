import pandas as pd
import numpy as np

dates = pd.date_range('20170901',periods=4)
df = pd.DataFrame(np.arange(16).reshape(4,4),index=dates,columns=['a','b','c','d'])
s = pd.Series([1,2,3,4],index=pd.date_range('20170901',periods=4))
print(df)
print('-------------')
df.loc['20170901','a']=66
print(df.loc['20170901','a'])
print('-------------')
df.iloc[2,2]=66
print(df)
#print('----------------')
#df.b[df.a>5]=0
#print(df)
print('----------------')
#df[df.a>5]=0
#print(df)
df['e']=np.nan
df['e']=pd.Series([1,2,3,4],index=pd.date_range('20170901',periods=4))
print(df)

