import numpy as np

array = np.array([[1,2,3],[4,5,6]],np.int32)
print(array)
print(array.ndim)
print(array.shape)
print(array.size)
print(array.dtype)

print("1-------------------")

a = np.array([[24,22,23,25]])
print(a)
print ("ndim",a.ndim)
print("dtype",array.dtype)


print("2-------------------")

a = np.zeros((3,4),np.int32)
print(a)
print ("ndim",a.ndim)
print("dtype",array.dtype)
print("3-------------------")

a= np.arange(10,20,3)
print(a)
print("4-------------------")


a = np.arange(24)
print(a)
print (a.ndim)             # a 现只有一个维度
# 现在调整其大小
b=a.reshape(4,6)
print(b)
print (b.ndim)
b = a.reshape(2,4,3)  # b 现在拥有三个维度
print(b)
print (b.ndim)

print("5-------------------")

a=np.linspace(1,10,6).reshape(2,3)
print(a)

print("6-------------------")
a= np.array([10,20,30,40])
b=np.arange(4)
print(b)
c= a+b
# c=np.tan(a)
print(c)

print("7-------------------")
a= np.array([[1,1],[0,1]])
b=np.arange(4).reshape((2,2))
print(a)
print(b)
print(a*b)
print(np.dot(a,b))
print(a.dot(b))
print("8-------------------")

a= np.random.random([2,4])
print(a)
print(np.sum(a))

print(np.sum(a,axis=0))
print("9-------------------")

a= np.arange(2,14).reshape((3,4))
print(a)
print(np.argmin(a))
print(np.argmax(a))
print(np.mean(a))
print(a.mean())
print(np.transpose(a))
print(a.T)
# print((a.T).dot(a))
print(np.clip(a,5,9))

print("10-------------------")
a=np.arange(3,15).reshape((3,4))
print(a)
print(a.ndim)
print(a[2])
# 以下这两种方式是一样的
print(a[1][1])
print(a[1,1])
# 第一行，第一列和第二列的数字
print(a[1,1:3])


print("11-------------------")
a=np.arange(3,15).reshape((3,4))
print(a)
# 迭代行
for row in a:
    print(row)

    # 迭代列
for col in a.T:
    print(col)
print(a.flatten())
for item in a.flat:
    print(item)


print("12-------------------")
a=np.array([1,1,1])
b=np.array([2,2,2])
c=np.vstack((a,b))#纵向相加
print("c=",c)
d=np.hstack((a,b))
print("d=",d)
# print(a.shape,d.shape)
print(a)
print(a.shape)
print(a[np.newaxis,:])
print(a[np.newaxis,:].shape)
print(a[:,np.newaxis])
print(a[:,np.newaxis].shape)


a=np.array([1,1,1])[:,np.newaxis]
b=np.array([2,2,2])[:,np.newaxis]
d=np.hstack((a,b))
print("d=",d)


c=np.concatenate((a,a,b,b),axis=0)
print(c)


print("13-------------------")

a= np.arange(12).reshape((3,4))
print(a)
print(np.split(a,3,axis=0))
# axis=0，表示沿着第 0 轴进行操作，即对每一列进行操作,即是横着切，但是计算时是逐列计算；axis=1，表示沿着第1轴进行操作，即对每一行进行操作，即是竖着切
# 横0纵1
# 计算时0列1行
# 纵向
print(np.split(a,2,axis=1))
# 不等的分割，总共四列分成三列
print(np.array_split(a,3,axis=1))
# vsplit是对列进行分割，横着切
print(np.vsplit(a,3))
print(np.hsplit(a,2))


print("14-------------------")
a=np.arange(4)
print(a)
b=a
c=a
d=b
a[0]=11
print(a)

b= a.copy()

print("15-------------------")

a = np.array([24]*4)
print(a)

print(np.eye(4))
x =  [(1,2,3),(4,5)]
a = np.asarray(x)
print (a)