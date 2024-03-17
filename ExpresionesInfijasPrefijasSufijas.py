from Pila import Pila

def infijaASufija(sentencia):
    precedencia = {}
    precedencia["*"] = 3
    precedencia["/"] = 3
    precedencia["+"] = 2
    precedencia["-"] = 2
    precedencia["("] = 1
    pilaOperadores = Pila()
    listaSufija = []
    listaSimbolos = sentencia.split()
    for simbolo in listaSimbolos:
        if simbolo in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or simbolo in "0123456789":
            listaSufija.append(simbolo)
        elif simbolo == "(":
            pilaOperadores.agregar(simbolo)
        elif simbolo == ")":
            tope = pilaOperadores.eliminar()
            while tope != "(":
                listaSufija.append(tope)
                tope = pilaOperadores.eliminar()
        else:
            while(not pilaOperadores.estaVacia()) and (precedencia[pilaOperadores.imprimir()] >= precedencia[simbolo]):
                listaSufija.append(pilaOperadores.eliminar())
            pilaOperadores.agregar(simbolo)
    while not pilaOperadores.estaVacia():
        listaSufija.append(pilaOperadores.eliminar())
        return " ".join(listaSufija)
print(infijaASufija("A+B+C+D"))
print(infijaASufija("(A+B)*C-(D-E)*(F+G)"))
