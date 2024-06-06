from classVehiculo import Vehiculo

class Van(Vehiculo):
    __tipoCarroceria: str

    def __init__(self, marca, mod, año, capac, numP, distance, tarifa, tipoCa):
        super().__init__(marca, mod, año, capac, numP, distance, tarifa)
        self.__tipoCarroceria = tipoCa
    
    def getTipoC(self):
        return self.__tipoCarroceria
    
    def getTarifaDeServicios(self):
        if self.getTipoC() == "minivan":
            importe = self.getTarifaBase() - (10*self.getTarifaBase()) / 100
            return importe
        else:
            importeNormal = self.getTarifaBase() + (2.5*self.getTarifaBase()) / 100
            return importeNormal