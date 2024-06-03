from ClaseDepartamento import Departamento

class Edificio:
    __IdEdi: int
    __Nombre: str
    __Direccion: str
    __NombreEmpresa: str
    __CantidadPisos: int
    __CantidadDeptos: int
    __departamento: list

    def __init__(self, idE, nombre, direc, nombreEmp, cantP, cantD):
        self.__IdEdi = idE
        self.__Nombre = nombre
        self.__Direccion = direc
        self.__NombreEmpresa = nombreEmp
        self.__CantidadPisos = cantP
        self.__CantidadDeptos = cantD
        self.__departamento = []

    def AgregarDpto(self, xidD, xidE, xnomb, xnumpi, xnumdpt, xcanth, xcantb, xsup):
        self.__departamento.append(Departamento(xidD, xidE, xnomb, xnumpi, xnumdpt, xcanth, xcantb, xsup))

    def getIdEdi(self):
        return self.__IdEdi
    
    def getNombre(self):
        return self.__Nombre
    
    def getDireccion(self):
        return self.__Direccion
    
    def getNombreEmpresa(self):
        return self.__NombreEmpresa
    
    def getCantiPiso(self):
        return self.__CantidadPisos
    
    def getCantiDpto(self):
        return self.__CantidadDeptos
    
    def ListarPropietarios(self):
        for undpto in self.__departamento:
            print(f"Departamento {undpto.getIdDpto()} - {undpto.getNombre()}")
    
    def getTotalSup(self):
        acum = 0.0
        for undpto in self.__departamento:
            acum += undpto.getSuperficie()
        return acum
    
    def BuscaPropietario(self, nomb):
        band = False
        i = 0
        while band is False and i < len(self.__departamento):
            if self.__departamento[i].getNombre() == nomb:
                band = True
            else:
                i += 1
        return band
    
    def getSuperficieXpropietario(self, nomb):
        acum = 0.0
        for undpto in self.__departamento:
            if undpto.getNombre() == nomb:
                acum += undpto.getSuperficie()
        return acum
    
    def BuscaNumPiso(self, numP):
        band = False
        i = 0
        while band is False and i < len(self.__departamento):
            if self.__departamento[i].getNumPiso() == numP:
                band = True
            else:
                i += 1
        return band
    
    def ListarDptoConCondicion(self, numP):
        cont = 0
        for undpto in self.__departamento:
            if undpto.getNumPiso() == numP:
                if undpto.getBaños() > 1 and undpto.getHabitaciones() == 3:
                    print(undpto)
                    cont += 1
        return cont