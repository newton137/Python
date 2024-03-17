import sklearn
import mglearn
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

mglearn.plots.plot_pca_illustration()
cancer = load_breast_cancer()
print(cancer.feature_names)
pca = PCA(n_components=2)
PCA.fit(cancer.data)
transformada = pca.transform(cancer.data)
print(cancer.data.shape)
print(transformada.shape)
mglearn.discrete_scatter(transformada[:,0],transformada[:,1],cancer.target)
plt.legend(cancer.target_names,loc = "best")
plt.xlabel("PCA1")
plt.ylabel("PCA2")

from sklearn.preprocessing import MinMaxScaler
escala = MinMaxScaler()
escala.fit(cancer.data)
escalada = escala.transform(cancer.data)
pca.fit(escalada)
transformada = pca.transform(escalada)
mglearn.discrete_scatter(transformada[:,0],transformada[:,1],cancer.target)
plt.legend(cancer.target_names,loc = "best")
plt.gca()
plt.xlabel("PCA1")
plt.ylabel("PCA2")