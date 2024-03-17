from sklearn import tree

atributos = [[140,1],[130,1],[150,0],[170,0]]
objeto = [1,1,0,0]
clasificador = tree.DecisionTreeClassifier()
clasificador = clasificador.fit(atributos,objeto)
print (clasificador.predict([[160,0]]))
