import pandas as pd
import numpy as np

dates = pd.date_range('20170901',periods=4)
df = pd.DataFrame(data=np.random.randn(4,4),index=dates,columns=['a','b','c','d'])
#print(df)
#print(df['a'],df.a)
#print(df['20170901':'20170902'])
#print(df.loc['20170901'])
#print(df.loc['20170901',['a','b']])

#print(df.iloc[[1,2],1:3])
print(df[df.a>0.5])