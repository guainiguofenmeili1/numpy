import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data =pd.read_excel('Student.xlsx',encoding='utf-8',header=0)
print(data)
print(data.ndim)
print(data.columns.tolist())

# a = data[['Name','Gender']]
# a = data['Name'][0]
# print(a)

# data.to_pickle('Student.pickle')



df1= pd.DataFrame(np.ones((3,4))*0,columns=['A','B','C','D'])
df2= pd.DataFrame(np.ones((3,4))*1,columns=['A','B','C','D'])
df3= pd.DataFrame(np.ones((3,4))*2,columns=['A','B','C','D'])
print(df1)
print(pd.concat([df1,df2,df3],axis=0,ignore_index=True))


# axis=1是左右，axis=0是上下
# join, ('inner', 'outer')
# df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
# df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d', 'e'], index=[2,3,4])
# res = pd.concat([df1, df2], axis=1, join='outer')
# res = pd.concat([df1, df2], axis=1, join='inner')

# print(res)

# join_axes
# res = pd.concat([df1, df2], axis=1, join_axes=[df2.index])

# print(res)



# append
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d', 'e'], index=[2,3,4])
# res = df1.append(df2, ignore_index=True)
# res = df1.append([df2, df3])
#
s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
res = df1.append(s1, ignore_index=True)
# print(res)




print("1------------------------")

# merge

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                                  'A': ['A0', 'A1', 'A2', 'A3'],
                                  'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                                    'C': ['C0', 'C1', 'C2', 'C3'],
                                    'D': ['D0', 'D1', 'D2', 'D3']})


print("left=",left)
print("right=",right)


res= pd.merge(left,right,on="key")
print("res=",res)

print("2------------------------")


# consider two keys
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                             'key2': ['K0', 'K1', 'K0', 'K1'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})




right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                              'key2': ['K0', 'K0', 'K0', 'K0'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
print(right)
res = pd.merge(left, right, on=['key1', 'key2'], how='inner')  # default for how='inner'
# res = pd.merge(left, right, on=['key1', 'key2'], how='outer')
# how = ['left', 'right', 'outer', 'inner']
# res = pd.merge(left, right, on=['key1', 'key2'], how='left')
print(res)

print("3------------------------")


# indicator
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
# res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
# give the indicator a custom name
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
print(res)



print("4------------------------")


# merged by index
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                                  'B': ['B0', 'B1', 'B2']},
                                  index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                                     'D': ['D0', 'D2', 'D3']},
                                      index=['K0', 'K2', 'K3'])
print(left)
print(right)
# left_index and right_index
# left_index和right_index必须都是true
res = pd.merge(left, right, left_index=True, right_index=True, how='outer')
# res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
print("res=",res)


print("5-----------------------")

# handle overlapping
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})

print(boys)
print(girls)
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='left')
print(res)

print("6-----------------------")


# plot data

# Series
# data = pd.Series(np.random.randn(1000), index=np.arange(1000))
# data = data.cumsum()
# # data.plot()
# # plt.show()
#
# # DataFrame
# data = pd.DataFrame(np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD"))
# data = data.cumsum()
# data.plot()
# plt.show()


# plot methods:
# 'bar', 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie'
# ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label="Class 1")
# data.plot.scatter(x='A', y='C', color='LightGreen', label='Class 2', ax=ax)
#
# plt.show()
#
# 根据结果：
# mean(axis=0)计算的是每一列平均值，
# mean(axis=1)计算的是每一行平均值。
# drop(0,axis=0)删除行，
# drop([‘col1’],axis=1)删除列。
# https://www.cnblogs.com/nxf-rabbit75/p/10044801.html
# https://blog.csdn.net/qq_16234613/article/details/76223188