from classVehiculo import Vehiculo

class Autobous(Vehiculo):
    __tipoDeServicio: str
    __turno: str

    def __init__(self, marca, mod, año, capac, numP, distance, tarifa, tipo, turno):
        super().__init__(marca, mod, año, capac, numP, distance, tarifa)
        self.__tipoDeServicio = tipo
        self.__turno = turno

    def getTipoS(self):
        return self.__tipoDeServicio
    
    def getTurno(self):
        return self.__turno
    
    def getTarifaDeServicios(self):
        if self.getTurno() == "noche" and self.getTipoS() == "turismo":
            importe = self.getTarifaBase() + (20*self.getTarifaBase()) / 100
            return importe
        else:
            importeNormal = self.getTarifaBase() + (5*self.getTarifaBase()) / 100
            return importeNormal
    