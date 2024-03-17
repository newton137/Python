import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

iris = load_iris()
caracteristicas = iris.data
etiquetas = iris.target
XTrain, XTest, YTrain, YTest = train_test_split(caracteristicas,etiquetas)
network = MLPClassifier(max_iter=1000,hidden_layer_sizes=(5,5))
network.fit(XTrain,YTrain)
print(network.score(XTest,YTest))

