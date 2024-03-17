from scipy.spatial import distance

def distanciaEuclidea(a,b):
    return distance.euclidean(a,b)

class Scratch:
    def fit(self,xEntrenamiento,yEntrenamiento):#datos de entrenamiento
        self.xEntrenamiento = xEntrenamiento#atributos de entrenamiento
        self.yEntrenamiento = yEntrenamiento#nombres de iris
    def predict(self,xTest):
        predicciones = []#arreglo que devolverá predicciones
        for x in xTest:#itera por los atributos de entrada
            predicciones.append(self.cercano(x))#añade las predicciones de cada conjunto de atributos al arreglo
        return predicciones
    def cercano(self,test):#determina la distancia más cercana entre atributos del test y atributos del entrenamiento
        mejor = distanciaEuclidea(test,self.xEntrenamiento[0])#distancia entre atributos del test y los primeros atributos del entrenamiento
        indice = 0#almacena el indice de la distancia más cercana
        for i in range(1,len(self.xEntrenamiento)):#itera cada conjunto de atributos de entrenamiento y obtiene la distancia con atributos del test
            candidato = distanciaEuclidea(test,self.xEntrenamiento[i])
            if candidato < mejor:#compara la menor distancia con la distancia actual
                mejor = candidato
                indice = i
        return self.yEntrenamiento[indice]#obtiene el nombre del iris

from sklearn import datasets
iris = datasets.load_iris()#carga flores

x = iris.data#atributos
y = iris.target#nombres

from sklearn.cross_validation import train_test_split
xEntrenamiento, xTest, yEntrenamiento, yTest = train_test_split(x,y, test_size = .5)

from sklearn.neighbors import KNeighborsClassifier#importa clasificador
clasificador = Scratch()

clasificador.fit(xEntrenamiento,yEntrenamiento)#entrenamiento del clasificador

prediccion = clasificador.predict(xTest)#predice los tipos de iris
print(prediccion)

from sklearn.metrics import accuracy_score
print(accuracy_score(yTest,prediccion))