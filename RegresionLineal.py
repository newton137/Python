import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

boston = load_boston()
x = np.array(boston.data[:,5])
y = np.array(boston.target)

plt.scatter(x,y,alpha = 1)

x = np.array([np.ones(506),x]).T
print(x)
b = np.linalg.inv(x.T @ x) @ x.T @ y

plt.plot([4,9],[b[0] + b[1]*4, b[0] + b[1]*9], c="red")
plt.show()