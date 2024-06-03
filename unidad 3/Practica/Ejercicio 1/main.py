from GestorEdificio import gestorEdi

def menu():
    op = None
    try:
        op=int(input("""
                                Menú De Opciones
                [1] Ingresa nombre de edificio para conocer propietarios de sus departamentos
                [2] Conocer superficie total cubierta de un edificio
                [3] Conocer superficie total de departamento/s de un propietario
                [4] Ingresa numero de piso para conocer deptos con mas de un baño y 3 dormitorios
                [0] SALIR
                -> """))
    except ValueError:
        print("Le pifieste al numerin")
    return op

if __name__=="__main__":
    ge = gestorEdi()
    ge.edificioCSV()
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            try:
                nomb1 = input("Ingresa el nombre del edificio: ")
                ge.ListarProp(nomb1)
            except AssertionError:
                print("No existe ese edificio pe")
        
        elif opcion == 2:
            try:
                iD = int(input("Igrese el ID del edificio: "))
                ge.ListarSuperficieTotal(iD)
            except ValueError:
                print("NUMERO ENTERO PE")
            except AssertionError:
                print("No existe edificio con esa id")
        
        elif opcion == 3:
            try:
                nomb2 = input("Ingresa el nombre del propietario")
                ge.ListarSuperficieXdpto(nomb2)
            except AssertionError:
                print("No existe esa persona")
            
        elif opcion == 4:
            try:
                piso = int(input("Ingresa el numero de piso: "))
                ge.mostrarDepartamentosConCondiciones(piso)
            except ValueError:
                print("NUMERO ENTERO PE")
            except AssertionError:
                print("No existe ese numero de piso")
        else:
            print("OPCION DE NABO")
        opcion = menu()