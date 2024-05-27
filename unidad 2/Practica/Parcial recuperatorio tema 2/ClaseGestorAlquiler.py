import csv
from ClaseAlquiler import Alquiler

class gestorAlquiler:
    __alquiler: list

    def __init__(self):
        self.__alquiler = []

    def AgregarAlquiler(self, unalquiler):
        self.__alquiler.append(unalquiler)

    def alquilerCSV(self):
        archivo = open("Alquiler.csv")
        reader = csv.reader(archivo, delimiter=';')
        bandera = False
        for fila in reader:
            if bandera is False:
                bandera = True
            else:
                unalquiler = Alquiler(fila[0], fila[1], fila[2], int(fila[3]), int(fila[4]))
                self.AgregarAlquiler(unalquiler)
        archivo.close()
        return self.__alquiler

    def EmitirListado(self, cancha):
        self.__alquiler = sorted(self.__alquiler, reverse=True)
        i = 0
        total = 0
        print("Hora  Id de Cancha  Duración alquiler  Importe por hora  Importe alquiler ")
        while i < len(self.__alquiler):
            texto = '{}\t{}\t\t{}\t\t\t{}\t\t{}'
            hora = f'{self.__alquiler[i].getHoras()}:{self.__alquiler[i].getMinutos()}'
            IdA = self.__alquiler[i].getId()
            duracion = self.__alquiler[i].getDuracion()
            impXh = cancha.ImporteXhora(IdA)
            ImpA = (duracion/60) * impXh
            horitas = duracion/60
            total += ImpA
            print(texto.format(hora, IdA, horitas, impXh, ImpA))
            i += 1
        print("Total recaudado:                                             {}" .format(total))

    def contarMinutos(self):
        cont = input("Ingrese ID de la cancha a mirar: ")
        acum = 0
        for alquiler in self.__alquiler:
            if alquiler.getId() == cont:
                acum += alquiler.getDuracion()
        print(f"El total de minutos jugas en la cancha {cont} fue de {acum}minutos")