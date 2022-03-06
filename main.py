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
