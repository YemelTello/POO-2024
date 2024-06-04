class Ladrillo:
    __alto= 7
    __largo= 25
    __ancho= 15
    __cantidad: int
    __identificador: int
    __kgMatPrimUti: float
    __costo: float
    __materiales: list

    def __init__(self, cant, ID, kg, costo):
        self.__cantidad = cant
        self.__identificador = ID
        self.__kgMatPrimUti = kg
        self.__costo = costo
        self.__materiales = []

    def agregarMaterial(self, unmaterial):
        if (unmaterial in self.__materiales) is False:
            self.__materiales.append(unmaterial)
            print(f"Al ladrillo {self.__identificador} se le agrega el material {unmaterial.getMaterial()}")
        else:
            print(f"No se agrega el material {unmaterial.getMaterial()} al ladrillo {self.__identificador} porque ya lo tiene")


    def getCantidad(self):
        return self.__cantidad
    
    def getId(self):
        return self.__identificador
    
    def getKg(self):
        return self.__kgMatPrimUti
    
    def getCosto(self):
        return self.__costo
    
    def ListarCostoyCaracteristicas(self):
        if len(self.__materiales) > 0:
            for unmaterial in self.__materiales:
                print(f"\nMaterial {unmaterial.getMaterial()}\n Costo: {unmaterial.getCosto()}\n Caracteristicas: {unmaterial.getCaracteristicas()}")
        else:
            print("El ladrillo con esa ID no usa material refractario")

    def getCostoTotal(self):
        acum = self.__costo
        for unmaterial in self.__materiales:
            acum += unmaterial.getCosto()
        return acum
    
    def getMateriales(self):
        retorna: str=""
        if len(self.__materiales) > 0:
            for unmaterial in self.__materiales:
                retorna += str(unmaterial.getMaterial()) + ","
        return retorna
    
    def getCostosAdicionales(self):
        retorna: str=""
        if len(self.__materiales) > 0:
            for unmaterial in self.__materiales:
                retorna += "$" + str(unmaterial.getCosto()) + ","
        return retorna
    
    @classmethod
    def getAlto(cls):
        return cls.__alto

    @classmethod
    def getLargo(cls):
        return cls.__largo

    @classmethod
    def getAncho(cls):
        return cls.__ancho