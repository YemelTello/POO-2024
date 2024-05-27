from ClaseReserva import Reserva
import csv

class GestorReserva:
    __reserva: list

    def __init__(self):
        self.__reserva = []

    def AgregarReserva(self, unareserva):
        self.__reserva.append(unareserva)

    def AlmacenarReservaCSV(self):
        archivo = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 2\\Practica\\Parcial recuperatorio tema 1\\Reservas.csv")
        reader = csv.reader(archivo,delimiter=";")
        bandera = False
        for fila in reader:
            if bandera is False:
                bandera = True
            else:
                unareserva = Reserva(int(fila[0]), fila[1], int(fila[2]), (fila[3]), int(fila[4]), int(fila[5]), float(fila[6]))
                self.AgregarReserva(unareserva)
        archivo.close()
        return self.__reserva
    
    def HAY_reserva(self, fecha):
        for reservita in self.__reserva:
            if reservita.getFecha() == fecha:
                return fecha
            else:
                return False
            
    def listado_reservas(self, cabaña, fecha):
        i=0
        while i < len(self.__reserva):
            if self.__reserva[i].getFecha()==fecha:
                texto="{}\t\t{}\t{}\t\t{}\t{}"
                imp_diario = cabaña.importe_diario(self.__reserva[i].getCabana()) 
                print(texto.format(self.__reserva[i].getCabana(),imp_diario,self.__reserva[i].getCantDia(),
                                   self.__reserva[i].getImporte(),(self.__reserva[i].getCantDia() * imp_diario - self.__reserva[i].getImporte()))) 
            i+=1