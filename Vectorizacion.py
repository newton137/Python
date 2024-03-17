from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

noticias = fetch_20newsgroups(subset="train")#carga el set de data
print(noticias.data[0])#imprime el primer elemento del set
print(noticias.target[0])#imprime la clasificacion del elemento de arriba
print(len(noticias.data))#imprime el tamaño del set de data
print(noticias.target_names)#imprime los nombres
vector = CountVectorizer()#carga la clase de vectorización
vector.fit(noticias.data)#llena la clase con la data
print(vector.vocabulary_)#cuenta las veces de palabras
bolsa = vector.transform(noticias.data)#empaqueta palabras en bolsas
bolsa.shape
bolsaY = noticias.target
XTrain,XTest,YTrain,YTest = train_test_split(bolsa,bolsaY)#divide la data
lr = LogisticRegression()#carga el algoritmo de regresión
lr.fit(XTrain,YTrain)#llena el algoritmo con data
print(lr.score(XTest,YTest))#predice con data test
