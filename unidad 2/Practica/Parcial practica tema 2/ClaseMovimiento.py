class Movimiento:
    __nroCuenta: int
    __fecha: str
    __descripcion: str
    __tipoDeMovimiento: str
    __Importe: float
    
    def __init__(self, nro, fecha, desc, tipo, importe):
        self.__nroCuenta = nro
        self.__fecha = fecha
        self.__descripcion = desc
        self.__tipoDeMovimiento = tipo
        self.__Importe = importe
        
    def getNro(self):
        return self.__nroCuenta
    
    def getFecha(self):
        return self.__fecha
    
    def getDescripcion(self):
        return self.__descripcion
    
    def getTipo(self):
        return self.__tipoDeMovimiento
    
    def getImporte(self): 
        return self.__Importe
    
    def __lt__(self, other):
        if isinstance(self, Movimiento) and isinstance(other, Movimiento):
            return self.__nroCuenta < other.getNro()