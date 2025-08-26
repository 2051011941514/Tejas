# data types for ndarrays 
import numpy as np 
arr1 = np.array([1,2,3],dtype = np.float64)
arr2 = np.array([1,2,3],dtype = np.int32)
print(f"{arr1.dtype}\n{arr2.dtype}")

# converting the data type of array with astype() function
arr3 = np.array([1,2,3,4,5])
print(arr3.dtype)
float_data = arr3.astype(np.float64)
print(float_data.dtype)
print(float_data)

numeric_string = np.array(["22.25","-25.25","123","-0.254"])
print(numeric_string.dtype)
numbers_string = numeric_string.astype(float)
print(numbers_string)
# giving datatype of another array 
int_array = np.arange(10)
calibers = np.array([.22, .270, .357, .380, .44, .50],dtype = np.float64)
int_array.astype(calibers.dtype)

# operations on arrays or vectorization 
"""
numpy enables us to perform the bath operation on data without using any loops 
this process is some users called it vectorization.
"""
import numpy as np 
arr_ = np.array([[1,2,3],[4,5,6]])
print(f"Addition of array:{arr_+arr_}\nMultiplication of array:{arr_*arr_},\nDivision of array{arr_/10}\nSubtraction on array : {arr_-arr_}")

# operations on array 
division = 1/arr_
print(f"{division},\n{arr_**2}")
arr__ = np.array([[7,8,9],[0,0.2,0.3]])
print(arr_>arr__)

# understanding np.arrange function 
arr_1 = np.arange(10)
print(arr_1)
# indexing and slicing Also known as broadcasting 
print(arr_1[5])
print(arr_1[5:8])
arr_1[5:8]=12
print(arr_1)

# slicing of arrays # if we are modefying sourece array it will reflect in main array 
slice_arr = arr_1[5:8]
print(slice_arr)
slice_arr[1] = 12345
print(arr_1)
# if you want to change whole array you can use [:]
slice_arr[:]=64
print(arr_1)

# 3-dimentional arrays 
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3d)
print(arr3d[0])
print(arr3d[0,1])
print(arr3d[0,1,2])
old_values = arr3d[0].copy()
arr3d[0] = 65
print(arr3d)
print(old_values)
arr3d[0]= old_values
print(arr3d)

# 21-08-2025 , 4:06pm ,Thursday 
# indexing with slices 
import numpy as np
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
print(arr2d[:])
print(arr2d[2:])
print(arr2d[:2])
print(arr2d[:1])
print(arr2d[1:2])
print(arr2d[2:,1:])
print(arr2d[:2,1:])
print(arr2d[0,1:])
lower_dim_size = arr2d[1,:2]
print(lower_dim_size.shape)
print(arr2d[:2,2])
print(arr2d)
print(arr2d[:,:1])
print(arr2d[:,1:])
print(arr2d[:2,1:])
arr2d[:2,1:] = 0
print(arr2d)
import numpy as np
# boolean indxing 
# 2:48pm , Friday, 22-08-2025
names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
data = np.array([[4,7],[0,2],[-5,6],[0,0],[1,2],[-12,-4],[3,4]])
print(data.shape)
print(data)
print(names)
print(names == "Bob")
print(data[names == "Bob"])
print(data[names == "Bob",1:])
print(data[names == "Bob",1])
print(names != "Bob")
print(~(names=="Bob"))
print(data[~(names == "Bob")])

# To select two of the three names to combine multiple Boolean conditions, use
# Boolean arithmetic operators like & (and) and | (or):
mask = (names =="Bob") | (names == "Will")
print(mask)
print(data[mask])

# setting negative values as zero 
data[data<0]= 0
print(data)
print(data[names != "Joe"])
data[names != "Joe"] = 7
print(data)

# fancy indexing 
arr = np.zeros((8,4))
for i in range(8):
    arr[i] = i

print(arr)

print(arr[[4,3,0,6]]) # from up 

print(arr[[-3,-5,-7]]) # from down 

arr = np.arange(32).reshape((8,4))

print(arr)
"""
Passing multiple index arrays does something slightly different; it selects a one
dimensional array of elements corresponding to each tuple of indices:
"""
print(arr[[1,5,7,2],[0,3,1,2]])
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])

# transposing arrays ans swaping axis 
arroda = np.arange(15).reshape(3,5)
print(arroda)
print(arroda.T)
soma = arroda.T
print(soma)
nrr = np.array([[0, 1, 0], [1, 2, -2], [6, 3, 2], [-1, 0, -1], [1, 0, 1
 ]])
print(nrr)
print(np.dot(nrr.T,nrr))
print(nrr.T @ nrr)

# another method of transposing # swapaxes(0,1)
print(nrr.swapaxes(0,1))