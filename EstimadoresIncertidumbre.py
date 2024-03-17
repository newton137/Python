from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import svm

iris = load_iris()
XTrain, XTest, YTrain, YTest = train_test_split(iris.data,iris.target)
support = svm.SVC(probability=True)
support.fit(XTrain,YTrain)
support.decision_function_shape = "ovr"
print(support.decision_function(XTest)[:10])
print(support.predict_proba(XTest)[:10])
print(support.predict(XTest)[:10])