from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer,load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz

import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
XTrain,XTest,YTrain,YTest = train_test_split(iris.data,iris.target)
arbol = DecisionTreeClassifier()
arbol.fit(XTrain,YTrain)
print(arbol.score(XTest,YTest))
print(arbol.score(XTrain,YTrain))
export_graphviz(arbol,out_file="arbol",class_names=iris.target_names,feature_names=iris.feature_names,impurity=False,filled=True)
with open("arbol") as a:
    grafica = a.read()

caract = iris.data.shape[1]
plt.barh(range(caract),arbol.feature_importances_)
plt.yticks(np.arange(caract),iris.feature_names)
plt.xlabel("Importancia de las características")
plt.ylabel("características")
plt.show()
    