#Persistencia de modelo
from sklearn import datasets,linear_model
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
clf = linear_model.LogisticRegression()
print(iris.keys())
XTrain,XTest,YTrain,YTest = train_test_split(iris.data,iris.target)
clf.fit(XTrain,YTrain)
clf.score(XTest,YTest)

from sklearn.externals import joblib
joblib.dump(clf,"ModeloLogisticRegressionEntrenado.pkl")