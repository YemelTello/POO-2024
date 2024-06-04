class Matricula:
    __Fecha: str
    __empleados: object
    __programas: object

    def __init__(self, fecha, empleado, programa):
        self.__Fecha = fecha
        self.__empleados = empleado
        self.__programas = programa

    def getFecha(self):
        return self.__Fecha
    
    def getEmpleado(self):
        return self.__empleados
    
    def getPrograma(self):
        return self.__programas