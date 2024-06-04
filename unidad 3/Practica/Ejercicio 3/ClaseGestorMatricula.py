from ClaseMatricula import Matricula
from random import choice

class gestorMatricula:
    __matriculas: list
    __fecha="04/06/2024"

    def __init__(self):
        self.__matriculas = []

    def agregarMatricula(self, unamatricula):
        self.__matriculas.append(unamatricula)

    def buscaMatricula(self, unamatricula):
        band = False
        i = 0
        while band is False and i < len(self.__matriculas):
            if(unamatricula.getEmpleado() == self.__matriculas[i].getEmpleado()) and (unamatricula.getPrograma() == self.__matriculas[i].getPrograma()):
                band = True
            else:
                i += 1
        return band
    
    def asignar(self, ge, gp):
        iE = list(range(ge.getEmpleados()))
        iP = list(range(gp.getProgramas()))
        for i in range(5):
            indiceE = choice(iE)
            indiceP = choice(iP)
            unamatricula = Matricula(self.getFecha(), ge.getEmpleadoXindice(indiceE), gp.getProgramasXindice(indiceP))
            if self.buscaMatricula(unamatricula) is False:
                self.agregarMatricula(unamatricula)
                ge.getEmpleadoXindice(indiceE).agregarMatricula(unamatricula)
                gp.getProgramasXindice(indiceP).agregarMatricula(unamatricula)
                print(f"{ge.getEmpleadoXindice(indiceE)} se matriculó en {gp.getProgramasXindice(indiceP)}")
            else:
                print(f"{ge.getEmpleadoXindice(indiceE)}, ya estaba matriculado en {str(gp.getProgramasXindice(indiceP))}, por lo tanto, no se matriculó")

    @classmethod
    def getFecha(cls):
        return cls.__fecha

    @classmethod
    def setFecha(cls,xfecha):
        cls.__fecha=xfecha