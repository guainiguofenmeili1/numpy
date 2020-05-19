import numpy as np
import pandas as pd
dates = pd.date_range("20190101",periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan
# any表示只要有一个是nan就去掉，all是只有所有都是nan才去掉
print(df.dropna(axis=0,how='any'))
# 默认值的概念
print(df.fillna(value=0))
print(df.isnull())
print( np.any(df.isnull())==True)
print(df)
print(pd.isnull("aa"))