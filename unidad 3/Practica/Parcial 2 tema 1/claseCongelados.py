from claseProducto import Producto

class Congelados(Producto):
    __composicion: str
    __metodo: str

    def __init__(self, nomb, fechaE, fechaV, temp, pais, num, costo, comp, met):
        super().__init__(nomb, fechaE, fechaV, temp, pais, num, costo)
        self.__composicion = comp
        self.__metodo = met

    def getComposicion(self):
        return self.__composicion
    
    def getMetodo(self):
        return self.__metodo
    
    def getImporteDeVenta(self):
        if self.getMetodo() == "mecánico":
            importeM = self.getCostoBase + (15*self.getCostoBase()) / 100
            return importeM
        elif self.getMetodo() == "criogénico":
            importeC = self.getCostoBase + (10*self.getCostoBase()) / 100
            return importeC
    
    