class Fraccion:
    def __init__(self,numerador,denominador):
        self.num = numerador
        self.den = denominador
    def imprimir(self):
        print(self.num,"/",self.den)
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def __add__(self,otraFraccion):
        self.nueNum = self.num * otraFraccion.den + self.den * otraFraccion.num
        self.nueDen = self.den * otraFraccion.den
        comun = mcd(self.nueNum,self.nueDen)
        return Fraccion(self.nueNum//comun,self.nueDen//comun)
    def __eq__(self,otra):
        num1 = self.num * otra.den
        num2 = self.den * otra.num
        return num1 == num2
def mcd(m,n):
        while m%n != 0:
            mViejo = m
            nViejo = n
            m = nViejo
            n = mViejo%nViejo
        return n
f1 = Fraccion(5,4)
f2 = Fraccion(10,8)
f1.imprimir()
print(f2)
f3 = f1 + f2
print(f3)
print(f1.__add__(f2))
print(f1==f2)