class NodoArbol:
    def __init__(self,clave,valor,izquierdo = None,derecho = None,padre = None):
        self.clave = clave
        self.valor = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo
    def tieneHijoDerecho(self):
        return self.hijoDerecho
    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self
    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self
    def esRaiz(self):
        return not self.padre
    def esHoja(self):
        return not (self.hijoIzquierdo or self.hijoDerecho)
    def tieneAlgunHijo(self):
        return self.hijoIzquierdo or self.hijoDerecho
    def tieneAmbosHijos(self):
        return self.hijoIzquierdo and self.hijoDerecho
    def reemplazarDatos(self,clave,valor,izquierdo,derecho):
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.clave = clave
        self.valor = valor
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self
            
class ArbolBinarioBusqueda:
        def __init__(self):
            self.raiz = None
            self.tamano = 0
        def longitud(self):
            return self.tamano
        def __len__(self):
            return self.tamano
        def __iter__(self):
            return self.raiz.__iter__
        def agregar(self,clave,valor):
            if self.raiz:
                self._agregar(self,clave,valor,self.raiz)
            else: 
                self.raiz = NodoArbol(clave,valor)
            self.tamano += 1
        def _agregar(self,clave,valor,nodoActual):
            if clave < nodoActual.clave:
                if nodoActual.tieneHijoIzquierdo():
                    self._agregar(clave,valor,nodoActual.hijoIzquierdo)
                else:
                    nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre = nodoActual)
            else:
                if nodoActual.tieneHijoDerecho():
                    self._agregar(clave,valor,nodoActual.hijoDerecho)
                else:
                    nodoActual.hijoDerecho = NodoArbol(clave,valor,padre = nodoActual)
                    
        def obtener(self,clave):
            if self.raiz:
                res = self._obtener(clave,self.raiz)
                if res:
                    return res.valor
                else:
                    return None
            else:
                return None
        def _obtener(self,clave,nodoActual):
            if not nodoActual:
                return None
            elif nodoActual.clave == clave:
                return nodoActual
            elif clave < nodoActual.clave:
                return self._obtener(clave,nodoActual.hijoIzquierdo)
            else:
                return self._obtener(clave,nodoActual.hijoDerecho)
        def __getitem__(self,clave):
            return self.obtener(clave)
        def __contains__(self,clave):
            if self._obtener(clave,self.raiz):
                return True
            else:
                return False
        def eliminar(self,clave):
            if self.tamano > 1:
                eliminarNodo = self._obtener(clave,self.raiz)
                if eliminarNodo:
                    self.remover(eliminarNodo)
                    self.tamano -= 1
                else:
                    raise KeyError("La clave no está en el árbol")
            elif self.tamano == 1 and self.raiz.clave == clave:
                self.raiz = None
                self.tamano -= 1
            else:
                raise KeyError("La clave no está en el árbol de búsqueda")
        def __item__(self,clave):
            self.eliminar(clave)
        def remover(self,clave,nodoActual):
            if nodoActual.esHoja():
                if nodoActual == nodoActual.padre.HijoIzquierdo:
                    nodoActual.padre.hijoIzquierdo = None
                else:
                    nodoActual.padre.hijoDerecho = None
            elif nodoActual.tieneAmbosHijos():
                sucesor = nodoActual.encontrarSucesor()
                sucesor.empalmar()
                nodoActual.clave = sucesor.clave
                nodoActual.valor = sucesor.valor
            else:
                if nodoActual.tieneHijoIzquierdo():
                    if nodoActual.esHijoIzquierdo():
                        nodoActual.hijoIzquierdo.padre = nodoActual.padre
                        nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
                    elif nodoActual.esHijoDerecho():
                        nodoActual.hijoIzquierdo.padre = nodoActual.padre
                        nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
                    else:
                        nodoActual.reemplazarDatos(nodoActual.hijoIzquierdo.clave,nodoActual.hijoIzquierdo.valor,nodoActual.hijoIzquierdo.hijoIzquierdo,nodoActual.hijoIzquierdo.hijoDerecho)
                else:
                    if nodoActual.esHijoIzquierdo():
                        nodoActual.hijoDerecho.padre = nodoActual.padre
                        nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                    elif nodoActual.esHijoDerecho():
                        nodoActual.hijoDerecho.padre = nodoActual.padre
                        nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                    else:
                        nodoActual.reemplazarDatos(nodoActual.hijoDerecho.clave,nodoActual.hijoDerecho.valor,nodoActual.hijoDerecho.hijoIzquierdo,nodoActual.hijoDerecho.hijoDerecho)
                        