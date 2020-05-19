import numpy as np
import pandas as pd

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20190101'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "tain", "test", "train"]),
                    'F': 1111,
                    'G': 2222})

print(df2)
print(df2.groupby("E").get_group('test'))
print(df2.groupby("E").get_group('test').reset_index())
print(df2.groupby("E").sum())
print(df2.groupby("E").sum()[['F']])
print(df2.groupby("E").aggregate(np.sum))
print(df2['G'].apply(lambda x: x + 1))
print(df2['G'].apply(int))
print(df2.groupby("E").sum().sort_values(by="A"))
print(df2.groupby("E").sum().reset_index().sort_values(by="A"))

print("--------------")

df = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                   'B': ['B0', 'B1', 'B2', 'B3'],
                   'C': ['C0', 'C1', 'C2', 'C3'],
                   'D': ['D0', 'D1', 'D2', 'D3']})
print(df)
drop_t = df.set_index('A', drop=True, append=False, inplace=False, verify_integrity=False)
print(drop_t)
no_drop_t = df.set_index('A', drop=False, append=False, inplace=False, verify_integrity=False)
print(no_drop_t)
#
reset_drop_t = drop_t.reset_index(drop=False)  # 索引列会被还原为普通列
print(reset_drop_t)
reset_no_drop_t = no_drop_t.reset_index(drop=True)  # 索引列会被还原为普通列
print(reset_no_drop_t)

# https://www.cnblogs.com/muhe221/articles/10885583.html
