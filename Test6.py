import datetime

import numpy as np
import pandas as pd
from pandas.tseries.offsets import MonthEnd

data = {'city': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Hangzhou', 'Chongqing'],
        'year': [2016, 2016, 2015, 2017, 2016, 2016],
        'population': [2100, 2300, 1000, 700, 500, 500]}
frame = pd.DataFrame(data, columns=['year', 'city', 'population', 'debt'])

# 使用apply函数, 如果city字段包含'ing'关键词，则'判断'这一列赋值为1,否则为0
frame['panduan'] = frame.city.apply(lambda x: 1 if 'ing' in x else 0)
print(frame)


list1 = [[1,2,3],[4,5,6]]
print(list1)

print("11111111111111111111111")

df = pd.DataFrame({
    'user_id':[1,2,1,3,3,],
    'content_id':[1,1,2,2,2],
    'tag':['cool','nice','clever','clever','not-bad']
})
df_sub_1= df[['user_id','content_id','tag']]
df_sub_1.drop_duplicates()
print(df_sub_1)

# df_sub_1.set_index('tag').to_dict()['user_id']
# print(df_sub_1)
print(df_sub_1['tag'].value_counts().to_dict())

print("22222222222222")
print(pd.Timestamp('20190101'))
print(pd.Timestamp(pd.Timestamp('20190101')))
b=datetime.datetime.strftime(pd.Timestamp(pd.Timestamp('20190101')),'%Y-%m')
print(b)
c=datetime.datetime.strftime(pd.Timestamp(pd.Timestamp('20190201'))+MonthEnd(-1*2),'%Y-%m')
print(c)


