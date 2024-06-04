from claseGestorEmpleado import gestorEmpleado
from ClaseGestorMatricula import gestorMatricula
from ClaseGestorProgramaCapacitacion import gestorPrograma

def menu():
    op=None
    try:
        op=int(input("""
                                    Menú de Opciones
        [1] Duracion de programa por empleado ingresado
        [2] Dar programa para saber quien esta matriculado
        [3] Listar empleado flojos que no estan matriculados en nada
        [0] Salir
        -> """))

    except ValueError:
        pass
    return op

def test():
    ge = gestorEmpleado()
    gm = gestorMatricula()
    gp = gestorPrograma()
    ge.cargaCSV()
    gp.cargaCSV()
    gm.asignar(ge, gp)
    opcion = menu()
    while opcion != 0:

        if opcion==1:
            try:
                ID=int(input("Ingresa su ID: "))
                ge.mostrarDuracion(ID)
            except ValueError:
                print("NUMERO ENTERO CRACK")
            except AssertionError:
                print("ESE ID NO EXISTE")

        elif opcion==2:
            try:
                nombre=input("Ingresa nombre de programa: ")
                gp.mostrarPrograma(nombre)
            except AssertionError:
                print("ESE PROGRAMA NO EXISTE")

        elif opcion==3:
            try:
                ge.mostrarEmpleadoFlojos()
            except ValueError:
                print("ERROR. NO HAY NINGUN FLOJO")

        else:
            print("OPCION NADA QUE VER, TRATA PONIENDO LAS QUE TE DOY")
        opcion=menu()

if __name__=="__main__":
    test()