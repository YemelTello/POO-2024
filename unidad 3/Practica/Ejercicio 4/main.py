from claseListaPublicacion import Lista
from claseLibro import Libro
from claseCD import CD

def menu():
    op=None
    try:
        op=int(input("""
                            Menú de Opciones
            [1] Agregar una publicacion
            [2] Tipo de publicacion
            [3] Mostrar cantidad de publicaciones
            [4] Mostrar Todo
            [0] SALIR
            -> """))
    except ValueError:
        pass
    return op

def test():
    L = Lista()
    L.cargaCSV()
    opcion = menu()
    while opcion != 0:

        if opcion == 1:
            try:
                publi = int(input("Tipo [1]: Libro,Tipo [2]: CD, [0]: Salir de esta opcion\n ->"))
                while publi != 0:
                    if publi != 0:
                        titulo = input("Ingrese titulo: ")
                        categoria = input("Ingrese su categoria: ")
                        precio = input("Ingrese precio base: ")

                        if publi == 1:
                            nombre=input('Nombre de Autor: ')
                            fecha=input('Fecha de Edicion (dd/mm/yyyy): ')
                            cantidad=int(input('Cantidad de Paginas: '))
                            nuevaPubicacion=Libro(tit=titulo,cat=categoria,pr=precio,nomb=nombre,Fecha=fecha,cant=cantidad)
                        elif publi == 2:
                            time=int(input('Tiempo de Reproduccion(en minutos): '))
                            narra=input('Nombre del Narrador: ')
                            nuevaPubicacion=CD(tit=titulo,cat=categoria,pr=precio,Time=time,narrador=narra)
                        L.agregarPublicacion(nuevaPubicacion)
                    else:
                        print("Ingrese 1 o 2")
                    publi = int(input("Tipo [1]: Libro,Tipo [2]: CD, [0]: Salir de esta opcion\n ->"))
            except ValueError:
                print("INGRESA UN NUMERO CAMPEON")

        elif opcion == 2:
            try:
                posicion = int(input("Ingrese la posicion: "))
                L.getPublicacion(posicion)
            except ValueError:
                print("INGRESA UN NUMERO CAMPEON")

        elif opcion == 3:
            L.mostrarCant()

        elif opcion == 4:
            L.mostrarTodo()

        else:
            print("TE EQUIVOCASTE DE NUMERO Kk")
        opcion = menu()

if __name__ == "__main__":
    test()