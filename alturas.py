import numpy as np
import matplotlib.pyplot as plt

mexicanos = 1000
estadounidenses = 1000

altMex = 1.70 + 0.1 * np.random.randn(mexicanos) 
altEst = 1.90 + 0.1 * np.random.randn(estadounidenses)

plt.hist([altMex,altEst], stacked = True, color = ["r","b"])
plt.show()