class Cuenta:
    __Apellido: str
    __Nombre: str
    __DNI: int
    __Telefono: int
    __Saldo: float
    __CVU: int
    PorcentajeAnual = 68
    
    def __init__(self, apellido, nombre, dni, telefono, saldo, cvu):
        self.__Apellido = apellido
        self.__Nombre = nombre
        self.__DNI = dni
        self.__Telefono = telefono
        self.__Saldo = saldo
        self.__CVU = cvu

    def getApellido(self):
        #Retorna el apellido
        return self.__Apellido
    
    def getNombre(self):
        #Retorna el nombre
        return self.__Nombre
    
    def getDNI(self):
        #Retorna numero de dni
        return self.__DNI
    
    def getTelefono(self):
        #Retorna numero de celular
        return self.__Telefono
    
    def getSaldo(self):
        #Retorna el saldo que hay en la cuenta
        return self.__Saldo
    
    def getCVUc(self):
        #Retorna numero de cvu
        return self.__CVU
    
    def getPorcentaje(self):
        #Retorna el porcentaje que hay para todas las cuentas
        return self.__PorcentajeAnual
    
    def actualizarSaldo_Transaccion(self, transacciones):
        self.__Saldo -= transacciones
        self.__Saldo = round(self.__Saldo, 2)

    def mostrarDatos(self):
        print(f"""
                DATOS
            Apellido: {self.__Apellido}
            Nombre: {self.__Nombre}
            CVU: {self.__CVU}
            Saldo: {self.__Saldo}
              """)