from numpy import exp, array,random, dot
class RedNeural:
    def __init__(self):
        random.seed(1)
        self.weights = 2*random.random((3,1))-1
    def train(self,entradas,salidas,numero):
        for iteracion in range(numero):
            salida = self.think(entradas)
            error = salidas - salida
            ajuste = dot(entradas.T, error*salida*(1-salida))
            self.weights += ajuste
    def think(self,entradas):
        return self.__sigmoid(dot(entradas,self.weights))
    def __sigmoid(self,x):
        return 1/(1 + exp(-1))
red = RedNeural()
entradas = array([[1,1,1],[1,0,1],[1,1,1]])
salidas = array([[1,1,0]]).T
red.train(entradas,salidas,10000)
print(red.think(array([1,0,0])))   