# multy dimension

import numpy as np

arr = np.array([[10, 20, 30], [10, 20, 40]])
print(arr)
print(type(arr))
print(arr.dtype)

for i in arr:
    print(i)

arr = np.linspace(0, 15, 16)
print(arr)

arr = np.arange(start=0, stop=10, step=1)
print(arr)

arr = np.zeros(10)
print(arr)

arr = np.ones(10)
print(arr)

# adding 5 to each
arr = np.array([10, 20, 50, 60, 90])
arr1 = np.array([10, 20, 50, 60, 90])
print(arr)

arr = arr + 5
print(arr)
print(arr)

print(np.sqrt(arr))
print(np.sign(arr))
print(np.cosh(arr))
print(np.max(arr))
print(np.min(arr))
print(np.concatenate([arr, arr1]))

arr2 = arr1
print(arr2)
print(id(arr1), id(arr2))  # BOTH are pointing same address

arr2_shadow_copy = arr1.view()  # shadow copy
print(arr2_shadow_copy)

arr2 = arr1.copy()  # deep copy
print(arr2)
print(id(arr1), id(arr2))  # BOTH are pointing same address

print("&&&&"*10)
nDimensionalArray = np.array(
    [
        [2, 4, 5],
        [5, 6, 8],
        [9, 7, 1],
    ]
)
print(nDimensionalArray)
print(nDimensionalArray.ndim)
print(nDimensionalArray.shape)
print(nDimensionalArray.size)

for i in nDimensionalArray:
    print(i)


arr3 = nDimensionalArray.flatten()
print(arr3)


# arr31 = nDimensionalArray.reshape(2,2,3)
# print(arr31)

m = np.matrix(nDimensionalArray)
print(m)
print(m.diagonal())
print(m.max())

# Keyworded Variable Length Arguments in Python
