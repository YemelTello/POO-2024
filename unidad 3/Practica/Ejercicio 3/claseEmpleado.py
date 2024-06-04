class Empleado:
    __NombreYapellido: str
    __iDempleado: int
    __Puesto: str
    __matriculas: list

    def __init__(self, nomb, iD, puesto):
        self.__NombreYapellido = nomb
        self.__iDempleado = iD
        self.__Puesto = puesto
        self.__matriculas = []

    def __str__(self):
        return f"Empleado: {self.__NombreYapellido} - ID: {self.__iDempleado}"
    
    def agregarMatricula(self, unamtricula):
        self.__matriculas.append(unamtricula)

    def getNombreE(self):
        return self.__NombreYapellido

    def getID(self):
        return self.__iDempleado

    def getPuesto(self):
        return self.__Puesto
    
    def getMatriculas(self):
        return len(self.__matriculas)
    
    def ListarEmpleado(self):
        if len(self.__matriculas) > 0:
            print(f"{self.__NombreYapellido} Matriculado en: ")
            for unamatri in self.__matriculas:
                curso = unamatri.getPrograma().getNombreP()
                duracion = unamatri.getPrograma().getDuracion()
                print(f"->{curso} , Dura: {duracion}")
        else:
            print("No esta matriculado")