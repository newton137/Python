from sklearn import decomposition,datasets
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

cancer = datasets.load_breast_cancer()#carga la data sobre tumores malignos y benignos
x = cancer.data#atributos
print(x)
sc = StandardScaler()
xTransformada = sc.fit_transform(x)#llena el escalador con atributos y los escala
print(xTransformada)
pca = decomposition.PCA(n_components = 2)#crea un Processing Component Analisys con 2 componentes
xPcaTransformada = pca.fit_transform(xTransformada)#la data se reduce a 2 atributos con la misma cantidad de filas
print(xPcaTransformada)
plt.legend(cancer.target_names,loc = "best")
plt.gca()
plt.xlabel("PCA1")
plt.ylabel("PCA2")
