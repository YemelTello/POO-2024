from claseRefrigerados import Refrigerados
from GestorProductos import gestorProducto
from claseCongelados import Congelados

def menu():
    op = None
    try:
        op=int(input("""
                                Menú De Opciones
                [1] Agregar producto
                [2] Ingresate una posicion y veras cosas magicas
                [3] Mostrar la cantidad de productos por tipo
                [4] Mostrar todo sobre los productos
                [0] SALIR
                -> """))
    except ValueError:
        print("Le pifieste al numerin")
    return op

def test():
    gp = gestorProducto()
    gp.cargaCSV()
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            try:
                unproducto = int(input("\n\tTipo [1]: REFRIGERADO\n \tTipo [2]: CONGELADO\n \t[0]: Salir de esta opcion\n -> "))
                while unproducto != 0 and unproducto == 1 or unproducto == 2:
                    if unproducto != 0:
                        nombre=input("Ingresa la nombre: ")
                        fechaEnv=input("Fecha de Envasado(dd/mm/aaaa): ")
                        fechaVenc=input("Fecha de vencimiento(dd/mm/aaaa): ")
                        temp=float(input("Temperatura de mantenimiento recomendada: "))
                        pais=input("País de origen: ")
                        numL=int(input("Numero de lote: "))
                        costoB=float(input("Costo Base: "))

                        if unproducto == 1:
                            cod = input("Codigo del organismo de supervision alimentaria: ").strip().lower()
                            nuevoProducto = Refrigerados(nombre, fechaEnv, fechaVenc, temp, pais, numL, costoB, cod)

                        else:
                            Comp = input("Composicion del aire con que fue congelado('%'de nitrógeno, '%'de oxígeno, '%'de dióxido de carbono y '%'de vapor de agua: ").strip().lower()
                            metodo = input("Metodo de congelacion(mecánico/criogénico): ")
                            nuevoProducto = Congelados(nombre, fechaEnv, fechaVenc, temp, pais, numL, costoB, Comp, metodo)
                        gp.agregarProducto(nuevoProducto)
                        print("VEHICULO AGREGADO")
                    else:
                        print("Ingrese 1 o 2")
                    unproducto = int(input("\n\tTipo [1]: REFRIGERADO\n \tTipo [2]: CONGELADO\n \t[0]: Salir de esta opcion\n -> "))
                print("SI ESTAS ACA INGRESASTE CUALQUIER COSA O INGRESASTE 0 PARA SALIR, MUY CAPO")
            except ValueError:
                print("INGRESA UN NUMERO CAMPEON")

        elif opcion == 2:
            try:
                posicion=int(input("Ingresa la posicion: "))
                gp.MostrarPosicion(posicion)
            except ValueError:
                print("INGRESA UN NUMERO CAMPEON")

        elif opcion == 3:
            gp.MostrarCadaTipo()

        elif opcion == 4:
            gp.MostrarTodo()
        
        else:
            print("OPCION NADA QUE VER")
        opcion = menu()

if __name__ == "__main__":
    test()