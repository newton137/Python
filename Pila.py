class Pila:
    def __init__(self):
        self.elementos = []#crea una lista vacia
    def estaVacia(self):
        return self.elementos == []
    def agregar(self,elemento):#se agrega nuevo elemento al final de  la lista
        self.elementos.append(elemento)
    def eliminar(self):#elimina elemento al final de la lista
        return self.elementos.pop()
    def imprimir(self):#imprime el ultimo de la lista
        return self.elementos[len(self.elementos)-1]
    def imprimirTodo(self):#imprime todos los elementos de la lista
        return self.elementos
    def tamano(self):#regresa el tamaño de la lista
        return len(self.elementos)

