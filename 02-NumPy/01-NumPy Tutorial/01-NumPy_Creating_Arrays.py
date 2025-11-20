import numpy as np

#Create a NumPy ndarray Object
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

print("--------------------")

#0-D Arrays
arr = np.array(42)
print(arr)

print("--------------------")

#1-D Arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)

print("--------------------")

#2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

print("--------------------")

#3-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

print("--------------------")

#Check Number of Dimensions?
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print('--------------------')

#Higher Dimensional Arrays
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('Number of dimensions: ', arr.ndim)