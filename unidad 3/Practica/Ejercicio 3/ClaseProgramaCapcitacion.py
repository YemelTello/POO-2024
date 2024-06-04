class Programa:
    __Nombre: str
    __Codigo: str
    __Duracion: int
    __matriculas: list

    def __init__(self, nomb, cod, drc):
        self.__Nombre = nomb
        self.__Codigo = cod
        self.__Duracion = drc
        self.__matriculas = []

    def agregarMatricula(self, unamtricula):
        self.__matriculas.append(unamtricula)

    def getNombreP(self):
        return self.__Nombre

    def getCodigo(self):
        return self.__Codigo
    
    def getDuracion(self):
        return self.__Duracion
    
    def listarEmpleados(self):
        if len(self.__matriculas) > 0:
            print("Empleado/s matriculado/s: ")
            for unamatri in self.__matriculas:
                print(f" -{unamatri.getEmpleado()}")
        else:
            print("No se matriculo nadie aca")
    
    @classmethod
    def getMatricula(cls):
        return cls.__matriculas