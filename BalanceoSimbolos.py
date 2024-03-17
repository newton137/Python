p = Pila()
print(p.estaVacia())
p.agregar(5)
p.agregar(7)
print(p.imprimirTodo())
print(p.tamano())
print(p.eliminar())
print(p.imprimir())

def verificarSimbolos(cadena):
    p = Pila()
    indice = 0
    balanceado = True
    while indice < len(cadena) and balanceado:
        simbolo = cadena[indice]
        if simbolo in "[{(":
            p.agregar(simbolo)
        else:
            if p.estaVacia():
                balanceado = False
            else:
                ultimo = p.eliminar()
                if not parejas(simbolo,ultimo):
                    return False
        indice += 1
    if balanceado and p.estaVacia():
        return True
    else:
        return False
    
def parejas(actual,ultimo):
    aperturas = "({["
    cierres = ")}]"
    return aperturas.index(ultimo) == cierres.index(actual)

print(verificarSimbolos("{([])}"))
print(verificarSimbolos("{]()"))