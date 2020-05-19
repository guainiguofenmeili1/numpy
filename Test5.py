import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# https://www.jianshu.com/p/23e7e9251abb
print(np.random.randn())
print(np.random.randn(10))
print(np.random.randn(2, 2))

print(pd.Series(np.random.rand(10)))
print("1----------------")

print(np.random.rand())
print(np.random.rand(10))
print(np.random.rand(2, 2))

print("2----------------")

print(np.ones((3, 4)) * 2)
print("2--------------------------------------")


df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Tim', 'Victor', 'Nick']})  # 构造原始数据文件
df = df.set_index('ID')  # 设置ID为索引生成一个新的Excel对象，并用df来引用它
df.to_excel('D:\\2.xlsx',sheet_name='Sheet1')  # 生成Excel文件，并存到指定文件路径下


print("3--------------------------------------")





a=[{'a1': 1, 'a2': 2, 'a3': 3},
 {'b1': 1, 'b2': 2, 'b3': 3},
 {'c1': 1, 'c2': 2, 'c3': 3}]
print([item[key] for item in a for key in item])

print("4--------------------------------------")
a=[{'a1': 1, 'a2':{'a':'1','b':'2'} , 'a3': '3'},
 {'a1': 1, 'a2': {'a':'2','b':'2'}, 'a3': '3'},
 {'a1': 1, 'a2': {'a':'3','b':'2'}, 'a3': '3'}]
# print([item[key] for item in a for key in item])
alist =[]
for item in a:
    # print(item.get('a2').get('a')+'/'+item.get('a3'))
    b = item.get('a2').get('a')+'/'+item.get('a3')

    alist.append(b)

print(alist)



df2 = pd.DataFrame({'a':alist,'b':alist})

print(df2)