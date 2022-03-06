# %%
import numpy as np
arr1 = np.arange(1000000)
l1 = list(range(1000000))
# %%
%time arr2 = arr1*2
# %%
%time l2 = [x * 2 for x in l1]
# %%
(data := np.random.randn(3, 4))
# %%
data * 10
# %%
data + data
# %%
data.shape
# %%
data.dtype
# %%
d1 = [10, 20, 5, 15]
(arr1 := np.array(d1))
# %%
d2 = [[1, 2, 3, 4], [4, 3, 2, 1]]
(arr2 := np.array(d2))
arr2.ndim
arr2.shape
# %%
np.zeros(10)
np.zeros((3,6))
np.empty((2, 3, 2))
np.arange(15)
np.full((2,2), 2.4)
np.eye(3)
# %%
arr = np.array([[1.0, 2.0, 3.0], [1.5, 2.5, 3.5]])
arr
arr * arr
arr - arr
1/arr
arr**0.5
arr3 = np.array([[1, 2, 3], [2, 2, 1], [3, 1, 1]])
np.linalg.inv(arr3)
# %%
arr = np.arange(10)
arr
arr[3]
arr[3:5]
arr[3:5] = 0
print(arr)
# %%
arr_slice = arr[0:3]
print(arr_slice)
arr_slice[0] = 100
print(arr)
# %%
arr_slice[:] = 200
print(arr)

# %%
arr2d = np.array([[1, 2, 3], [1, 1, 1], [2, 2, 2]])
print(arr2d)
print('***')
print(arr2d[0])
print('***')
print(arr2d[0,2])
print('***')
print(arr2d[0][2])
print('***')
# %%
arr = np.arange(0, 10)
print(arr)
arr[1:5]
arr2d[:2]
# %%
arr2d[:2, 1:]
# %%
arr2d[1, :2]
arr2d[:2, 2]

# %%
arr = np.arange(10)
print(arr)
np.sqrt(arr)
np.exp(arr)
# %%
x = np.random.randn(10)
y = np.random.randn(10)
np.maximum(x, y)
# %%
arr = np.random.randn(10, 20)
remainder, whole_part = np.modf(arr)
print(f'{remainder=}')
print(f'{whole_part=}')
# %%
x = np.array([[1.0, 4.0, 9.0], [4.0, 2.0, 1.0]])
y = np.array([[10.0, 9.0], [5.0, 2.0], [8.0, 1.0]])
print(f'{x=}')
print(f'{y=}')
# %%
x.dot(y)
np.dot(x, y)
np.dot(x, np.ones(3))
x @ np.ones(3)
# %%
from numpy.linalg import inv, qr
(x := np.random.randn(3, 3))
mat = x.T.dot(x)
print(mat)
inv(mat)
mat.dot(inv(mat))
q, r = qr(mat)
print(f'{q=}')
print(f'{r=}')
# %%
