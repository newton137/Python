class CompuertaLogica:
    def __init__(self,n):
        self.etiqueta = n
        self.salida = None
    def obtenerEtiqueta(self):
        return self.etiqueta
    def obtenerSalida(self):
        self.salida = self.ejecutarLogicaDeCompuerta()
        return self.salida
class CompuertaBinaria(CompuertaLogica):
    def __init__(self,n):
        CompuertaLogica.__init__(self,n)
        self.pinA = None
        self.pinB = None
    def obtenerPinA(self):
        if self.pinA == None:
            return int(input("Ingrese pin A para entrada a compuerta"+self.obtenerEtiqueta()+"-->"))
        else:
            return self.pinA.obtenerFuente().obtenerSalida()
    def obtenerPinB(self):
        if self.pinB == None:
            return int(input("Ingrese pin B para entrada a compuerta"+self.obtenerEtiqueta()+"-->"))
        else:
            return self.pinB.obtenerFuente().obtenerSalida()
class CompuertaUnaria(CompuertaLogica):
    def __init__(self,n):
        CompuertaLogica.__init__(self,n)
        self.pin = None
    def obtenerPin(self):
        if self.pin == None:
            return int(input("Ingrese pin para entrada a compuerta"+self.obtenerEtiqueta()+"-->"))
        else:
            return self.pin.obtenerFuente().obtenerSalida()
class CompuertaAnd(CompuertaBinaria):
    def __init__(self,n):
        CompuertaBinaria.__init__(self,n)
    def ejecutarLogicaDeCompuerta(self):
        a = self.obtenerPinA()
        b = self.obtenerPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0
class CompuertaOr(CompuertaBinaria):
    def __init__(self,n):
        CompuertaBinaria.__init__(self,n)
    def ejecutarLogicaDeCompuerta(self):
        a = self.obtenerPinA()
        b = self.obtenerPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0
class CompuertaNot(CompuertaUnaria):
    def __init__(self,n):
        CompuertaUnaria.__init__(self,n)
    def ejecutarLogicaDeCompuerta(self):
        a = self.obtenerPin()
        if a == 1:
            return 0
        else:
            return 1
class Conector():
    def __init__(self,deCom,aCom):
        self.deCompuerta = deCom
        self.aCompuerta = aCom
        aCom.asignarProximoPin(self)
    def obtenerFuente(self):
        return self.deCompuerta
    def obtenerDestino(self):
        return self.aCompuerta
    def asignarProximoPin(self,fuente):
        if self.pinA == None:
            self.pinA = fuente
        elif self.pinB == None:
            self.pinB = fuente
        else:
            raise RuntimeError("ERROR: Pines no disponibles")
y = CompuertaAnd("c1")
print(y.obtenerSalida())
z = CompuertaOr("c2")
print(z.obtenerSalida())
x = CompuertaNot("c3")
print(x.obtenerSalida())
c = Conector(y,x)
print(c)