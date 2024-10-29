import numpy as np

x = [5, 9, 16, 21, 27]
y = [25, 45, 66, 97, 134]

cov_mat = np.stack((x, y), axis = 0)
print(cov_mat)
print(np.cov(cov_mat))