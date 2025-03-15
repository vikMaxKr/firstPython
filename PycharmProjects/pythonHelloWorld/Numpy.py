#Numpy most useful feature is n dimentional array object aka ndarray
import sys

import numpy as np
from pandas import PeriodIndex

#Benefit of numpy array over python list:
# 1.Less memory
# 2. Fast
# 3. convenient

a=np.array([1,2,3])

python_arr=range(1000)
npy_arr=np.arange(1000)

print(sys.getsizeof(5)*len(python_arr))       # size of each element is 14bytes
print(npy_arr.size*npy_arr.itemsize)          #size of each element is 4 byte

###################################
# n1=np.array([1,2,3,4])
# n2=np.array([9,8,7,2])
#
# arr1=n1+n2
# arr2=n1*n2
# arr3=n1-n2
#
# print(arr1)
# print(arr2)
# print(arr3)
#
# #2D
#
# n12=np.array([[1,2,3],[4,5,6],[2,3,4]])
#
# print(n12.ndim)
# print(n12.itemsize)
# print(n12.dtype)
#
# n12=np.array([[1,2,3],[4,5,6],[2,3,4],[1,1,1]], dtype=np.float64)  #assigning 64 bit float
#
# print(n12.dtype)
# print(n12.shape)
#
# print(np.ones((3,4)))
#
# print(np.arange(0,4))
#
# print(np.arange(0,10,2))  #skip each two
#
# print(np.linspace(1,10,12))
#
# #re-shape
# n12.reshape(4,3)
# print(n12.shape)
#
# #flat array
#
# print(n12.ravel())
# print(n12.min())
# print(n12.sum())
# print(n12.sum(axis=0))
# print(n12.sum(axis=1))
# print(np.sqrt(n12))
#
# print(np.std(n12))  #standard deviation
#
# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# print()
# print()
# print(a+b)
# print(a*b)
#
# print(a.dot(b))   #dot product of matrix


###### Indexing and slicing

sl=np.array([1,2,3,4,5])
print(sl[1:])
print(sl[-1:])

sl2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(sl2[0:2,2])
print(sl2[-1,0:2])
print(sl2[:])        #all elements
print(sl2[:3])     # all elements below index 3

print(sl2[:,0:2])

for row in sl2:
    print(row)

for cell in sl2.flat:
    print(cell)

# print(np.vstack((sl2,sl2)))
# print(np.hstack((sl2,sl2)))

print(np.hsplit(sl2,3))

aa=np.arange(12).reshape(3,4)

print(aa)

bb=aa>5

print(bb)

print(aa[bb])

aa[bb]=-1


#--------vector

print()
print()
# a=np.zeros(4)
# print(f"a= {a}, shape= {a.shape}")
# a=np.zeros((4,))
# print(f"a= {a}, shape= {a.shape}")
#
# a=np.random.random_sample(4)
# print(f"a= {a}, shape= {a.shape}")

a=np.arange(6.)
print(f"a= {a}, shape= {a.shape}")

a=np.random.rand(4)

print(f"a= {a}, shape= {a.shape}")

#------------vector operation--------------

a=np.arange(10)
print(a[-1])

b=-a
print(a+b)

# dot product

x=0

print(a.shape[0])

for i in range(a.shape[0]):
    x=x+(a[i]*b[i])


print(x)

# C=np.array([[1,2,3,4],[2,4,6,5]])
#
# print("shape---",C.shape[1])

X=np.array([[1,2],[2,3],[3,4],[4,5]])
w=np.array([2,3])
c=np.dot(X[1],w)
#
# print(f"X[1] shape {X[1].shape}")
#
# print(f"w shape {w.shape}")

a=np.zeros((1,5))        #row and column one row and 5 column
print(a)

a=np.ones((2,2))

print(a)



