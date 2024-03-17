from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

iris = load_iris()
print(iris.feature_names)#nombre de los atributos
print(iris.target_names)#nombre de las flores
print(iris.data[0])#valores del atributo
print(iris.target[0])
for i in range(len(iris.target)):
    print("Ejemplo %d: Nombre %s, Atributos %s" %(i,iris.target[i],iris.data[i]))
indicesTest = [i for i in range(0,101,50)]

#Entrenamiento de la máquina
borrarTarget = np.delete(iris.target,indicesTest)
borrarData = np.delete(iris.data,indicesTest,axis = 0)

#Test
testTarget = iris.target[indicesTest]
testData = iris.data[indicesTest]

clasificador = tree.DecisionTreeClassifier()
clasificador.fit(testData,testTarget)
print(testTarget)
print(clasificador.predict(testData))
print(testTarget[0], testData[0])   