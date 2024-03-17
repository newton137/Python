from Pila import Pila

def resolver(expresionSufija):
    pilaOperandos = Pila()
    listaSimbolos = expresionSufija.split()
    for simbolo in listaSimbolos:
        if simbolo in "0123456789":
            pilaOperandos.agregar(int(simbolo))
        else:
            operandoDos = pilaOperandos.eliminar()
            operandoUno = pilaOperandos.eliminar()
            resultado = hacerAritmetica(simbolo,operandoUno,operandoDos)
            pilaOperandos.agregar(resultado)
    return pilaOperandos.eliminar()

def hacerAritmetica(operador,operandoIzquierda,operandoDerecha):
    if operador == "*":
        return operandoIzquierda * operandoDerecha
    elif operador == "/":
        return operandoIzquierda / operandoDerecha
    elif operador == "+":
        return operandoIzquierda + operandoDerecha
    else:
        return operandoIzquierda - operandoDerecha

print(resolver("5 4 + 7 8 + /"))
    