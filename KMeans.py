from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn import metrics

iris = datasets.load_iris()#carga la data
x = iris.data#guarda data en x
y = iris.target#guarda clasificacion en y
km = KMeans(n_clusters = 3,max_iter = 11000)#grupos en que se clasifica, numero maximo de iteraciones
km.fit(x)#entrena al algoritmo
predicciones = km.predict(x)#predice los datos
print(predicciones)
acertadas = metrics.adjusted_rand_score(y,predicciones)#compara respuestas correctas con predicciones
print(acertadas)