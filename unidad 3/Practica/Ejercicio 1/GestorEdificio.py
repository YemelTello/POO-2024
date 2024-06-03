from ClaseEdificio import Edificio
import csv

class gestorEdi:
    __edificios: list
    
    def __init__(self):
        self.__edificios = []

    def AgregarEdificio(self, unedificio):
        self.__edificios.append(unedificio)

    def edificioCSV(self):
        archivo = None
        try:
            archivo = open("F:\\Users\\yemel\\Desktop\\Universidad\\2do AÑO\\Programación Orientada a Objetos\\unidad 3\\Practica\\Ejercicio 1\\EdificioNorte.csv")
            reader = csv.reader(archivo, delimiter=";")
            unedificio = None
            for fila in reader:
                if len(fila) == 6:
                    unedificio = Edificio(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]),int(fila[5]))
                    self.AgregarEdificio(unedificio)
                else:
                    unedificio.AgregarDpto(int(fila[0]),int(fila[1]),fila[2],int(fila[3]),int(fila[4]),int(fila[5]),int(fila[6]),float(fila[7]))
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
        except PermissionError:
            print("No tienes permisos para leer el archivo.")
        except csv.Error as e:
            print(f"Error al procesar el archivo CSV: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
        finally:
            if archivo:
                archivo.close()

    def ListarProp(self, nomb):
        band = False
        i = 0
        while band is False and i < len(self.__edificios):
            if self.__edificios[i].getNombre() == nomb:
                self.__edificios[i].ListarPropietarios()
                band = True
            else:
                i += 1
        assert band is True, "band no es true xd"

    def ListarSuperficieTotal(self, iD):
        band = False
        i = 0
        while band is False and i < len(self.__edificios):
            if self.__edificios[i].getIdEdi() == iD:
                print("La superficie total es: ", self.__edificios[i].getTotalSup())
                band = True
            else:
                i += 1
        assert band is True, "band no es true xd"

    def ListarSuperficieXdpto(self, nomb):
        band = False
        for unedificio in self.__edificios:
            if unedificio.BuscaPropietario(nomb) is True:
                print(f"Es propietario de departamento/s en el edificio {unedificio.getIdEdi()}")
                print(f"La superficie total de dichos deptos es {unedificio.getSuperficieXpropietario(nomb)}")
                print(f"Que representa el %{round((unedificio.getSuperficieXpropietario(nomb)*100)/unedificio.getTotalSup(),2)} de la superficie total del edificio\n")
                band=True
        assert band is True, "band no es true xd"

    def mostrarDepartamentosConCondiciones(self, numP):
        band= False
        for unedificio in self.__edificios:
            if unedificio.BuscaNumPiso(numP) is True:
                cantidad = unedificio.ListarDptoConCondicion(numP)
                print(f"\nPor lo tanto {cantidad} departamentos cumplen esas condiciones en el edificio {unedificio.getIdEdi()}\n")
                band=True
        assert band is True