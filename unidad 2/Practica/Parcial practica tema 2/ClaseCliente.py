class Cliente:
    __nombre: str
    __apellido: str
    __dni: int
    __numeroCuenta: int
    __saldoAnterior: float
    
    def __init__(self, nombre, apellido, dni, nro, saldo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__numeroCuenta = nro
        self.__saldoAnterior = saldo
        
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDNI(self):
        return self.__dni
    
    def getCuenta(self):
        return self.__numeroCuenta
    
    def getSaldo(self):
        return self.__saldoAnterior
    
    def setSaldo(self,saldo):
        self.__saldoAnterior = saldo
        