import numpy as np
import pandas as pd


a=pd.Series(1,index=list(range(5)))
print(a)
#
s=pd.Series([1,2,3,np.nan,"44"])
print(s)
print(s.values)
print ("ndim",s.ndim)
# print(s.dtype)




# df1= pd.DataFrame(np.arange(12).reshape((3,4)))
# print(df1)



df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20190101'),
                    'C':pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D':np.array([3]*4, dtype='int32'),
                    'E':pd.Categorical(["test", "tain", "test", "train"]),
                    'F':'foo'})
print("df2=",df2)
print("df2.dtypes=",df2.dtypes)
print("df2.index=",df2.index)
print("df2.columns=",df2.columns)
print("df2.values=",df2.values)
print("df2.values.tolist()=",df2.values.tolist())

print("df2.describe=",df2.describe())
print("df2.T=",df2.T)
print("df2.sort_index=",df2.sort_index(axis=1,ascending=False))
print("df2.sort_index=",df2.sort_index(axis=0,ascending=False))
print("df2.sort_value=",df2.sort_values(by="E"))
print("df2.A=",df2.A,df2["B"][0])
# print(df2[True])
print("df2[0:4]",df2[0:4])

print("1---------------------")

dates = pd.date_range("20190101",periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
print("df['A']['20190101']=",df['A']['20190101'])
print("df.A=",df.A,df[df.B==1])
print("df[0:3]",df[0:2],df['20190101':'20190103'])
print("df.loc['20190101']",df.loc['20190101'])
print("df.loc",df.loc[:,['A','B']])
print("df.loc",df.loc['20190101',['A','B']])
# 表示第三行的数据
print("df.iloc[3]",df.iloc[3])
print("df.iloc[3,1]",df.iloc[3,1])

print("df.iloc[3:5,1:3]",df.iloc[3:5,1:3])
print("df.iloc[[3,4,5],1:3]",df.iloc[[3,4,5],1:3])

# ix不能使用了
# print(df.ix[:3,['A','C']])
print("22----------")
print(df.A>8)
print(df[df.A>8])

# 设置值
df.iloc[2,2]=1111
df.loc['20190101','B']=2222
df.B[df.A>4]=0
df['F']=np.nan

dates = pd.date_range("20190101",periods=6)
print(dates)
df['E'] = pd.Series([1,2,3,4,5,6],index=dates)
print(df)




