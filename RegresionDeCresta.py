import numpy as np
import matplotlib.pyplot as mpl
from sklearn import linear_model
x = 1. / (np.arange(1,11) + np.arange(0,10)[:,np.newaxis])
y = np.ones(10)
numAlphas = 200
alphas = np.logspace(-10,-2,numAlphas)
coeficientes = []
for a in alphas:
    ridge = linear_model.Ridge(alpha = a, fit_intercept = False)
    ridge.fit(x,y)
    coeficientes.append(ridge.coef_)
ax = mpl.gca()
ax.plot(alphas,coeficientes)
ax.set_xscale("log")
ax.set_xlim(ax.get_xlim()[::-1])
mpl.xlabel("alpha")
mpl.ylabel("weight")
mpl.title("Regresión de Cresta")
mpl.axis("tight")
mpl.show()