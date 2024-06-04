from gestoLadrillos import gestorLadrillo
from gestorMateriales import gestorMaterial

def menu():
    op = None
    try:
        op=int(input("""
                                Menú De Opciones
                [1] 
                [2] 
                [3] 
                [0] SALIR
                -> """))
    except ValueError:
        print("Le pifieste al numerin")
    return op

if __name__ == "__main__":
    GL = gestorLadrillo()
    GM = gestorMaterial()
    GL.cargaCSV()
    GM.cargaCSV()
    GL.asignarMateriales(GM)
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            xid = int(input("\nIngrese id de ladrillo: "))
            GL.mostrarLadrillos(xid)
        
        elif opcion == 2:
            GL.mostrarTotal()

        elif opcion == 3:
            GL.mostrarFabricados()

        else:
            print("OPCION NADA QUE VER, REINTENTA PROBANDO CON LAS QUE TE DOY")
        opcion = menu()