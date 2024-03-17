import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()
diabetesX = diabetes.data[:,np.newaxis,2]
diabetesXTrain = diabetesX[:-50]
diabetesXTest = diabetesX[-50:]
diabetesYTrain = diabetes.target[:-50]
diabetesYTest = diabetes.target[-50:]
regresion = linear_model.LinearRegression()
regresion.fit(diabetesXTrain, diabetesYTrain)
diabetesYPred = regresion.predict(diabetesXTest)
print("Coeficientes", regresion.coef_())
print("Error del cuadrado medio %.2f" % mean_squared_error(diabetesYTest, diabetesYPred))
plt.scatter(diabetesXTest,diabetesYTest,color="red")
plt.plot(diabetesXTest, diabetesYPred, color = "blue", linewidth = 3)
plt.xticks(())
plt.yticks(())
plt.show()