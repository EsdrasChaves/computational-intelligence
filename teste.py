import numpy as np

x = np.array([1, 2, 3])
print(x)

y = np.array([3, 2, 1])
print(y)

x[1] = y[0]

print(x)
print(y)