from claseProducto import Producto
from datetime import datetime

class Refrigerados(Producto):
    __codigo: int

    def __init__(self, nomb, fechaE, fechaV, temp, pais, num, costo, cod):
        super().__init__(nomb, fechaE, fechaV, temp, pais, num, costo)
        self.__codigo = cod

    def getCodigo(self):
        return self.__codigo
    
    def getImporteDeVenta(self):
        fechaVenc = datetime.strptime(self.getFechaVencimiento(), "%d/%m/%Y")
        hoy = datetime.now()
        dif = fechaVenc - hoy
        if dif.days <= 60:
            importe1 = self.getCostoBase() - (10*self.getCostoBase()) / 100
            return importe1
        else:
            importe2 = self.getCostoBase() - (1*self.getCostoBase()) / 100
            return importe2