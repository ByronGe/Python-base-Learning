import pandas as pd
import numpy as np

df1=pd.DataFrame(np.ones((3,4)),columns=['a','b','c','d'])
df2=pd.DataFrame(np.zeros((3,4)),columns=['a','b','c','d'])
res = pd.concat([df1,df2],ignore_index=True,join='inner')
#print(res)

df3=pd.DataFrame(np.ones((3,4)),columns=['c','d','e','f'],index=[1,2,3])
df4=pd.DataFrame(np.zeros((3,4)),columns=['a','b','c','d'],index=[2,3,4])

res2 = pd.concat([df4,df3],axis=1,join_axes=[df4.index])
print(res2)