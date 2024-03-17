from Pila import Pila
def convertirABinario(decimal):
    residuoLista = Pila()
    while decimal > 0:
        residuo = decimal % 2
        residuoLista.agregar(residuo)
        decimal = decimal // 2
    cadenaBinaria = ""
    while not residuoLista.estaVacia():
        cadenaBinaria = cadenaBinaria + str(residuoLista.eliminar())
    return cadenaBinaria
print(convertirABinario(255))

def convertirABase(decimal,base):
    simbolos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    residuoLista = Pila()
    while decimal > 0:
        residuo = decimal % base
        residuoLista.agregar(residuo)
        decimal = decimal // base
    cadena = ""
    while not residuoLista.estaVacia():
        cadena = cadena + simbolos[residuoLista.eliminar()]
    return cadena
print(convertirABase(26,26))