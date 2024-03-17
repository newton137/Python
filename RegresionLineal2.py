from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Ridge

boston = load_boston()
boston.keys()
print(boston.target.shape)
XTrain,XTest,YTrain,YTest = train_test_split(boston.data,boston.target)
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(XTrain,YTrain)
print(knn.score(XTest,YTest))
lr = LinearRegression()
lr.fit(XTrain,YTrain)
print(lr.score(XTest,YTest))
print(lr.score(XTrain,YTrain))
del knn,lr
ridge = Ridge(alpha=1.0)
ridge.fit(XTrain,YTrain)
print(ridge.score(XTest,YTest))
del ridge