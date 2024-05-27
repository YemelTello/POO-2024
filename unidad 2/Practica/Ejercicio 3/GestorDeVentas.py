from ClaseGestor import GestorVenta

def opcion1(self,dia,num,imp):
    """Metodo para la opcion 1"""
    self.__arreglo[num-1][dia-1]+=imp
    print("El nuevo importe es: ",self.__arreglo[num-1][dia-1])

def opcion2(self,num):
    """Metodo para la opcion 2"""
    acum=0
    for i in range(7):
        acum+=self.__arreglo[num-1][i]
    print(f"El total recaudado por la sucursal {num} es: ",round(acum,2))

def opcion3(self,dia):
    """Metodo para la opcion 3"""
    max=-1.5
    for i in range(5):
        if self.__arreglo[i][dia-1]>max:
            max=self.__arreglo[i][dia-1]
            auxMax=i+1
    print("La sucursal que mas facturo ese dia fue la ",auxMax)

def opcion4(self):
    """Metodo para la opcion 4"""
    min=9999999999999
    for i in range(5):
        for j in range(7):
            if self.__arreglo[i][j]<min:
                min=self.__arreglo[i][j]
                auxMin=i+1
    print("La sucursal con menos facturacion durante la semana fue la ",auxMin)

def opcion5(self):
    """Metodo para la opcion 5"""
    acum=0
    for i in range(5):
        for j in range(7):
            acum+=self.__arreglo[i][j]
    print("El total acumulado por todas las sucursales durante la semana es ",acum)


def menu():
    op=int(input("""
                                 MENÚ DE OPCIONES
          [1] Ingresa dia, numero e importe. Acumular para ese dia y sucursal
          [2] Ingresa sucursal. Calcular su total de facturacion
          [3] Ingresa dia. Mostrar sucursal que mas facturó ese dia
          [4] Calcular sucursal con menos facturacion durante la semana
          [5] Calcular el total facturado por todas las sucursales
          [0] SALIR
          -> """))
    return op

def carga():
    #Carga los datos de las ventas
    for i in range(5):
         for j in range(7):
              print(input("Ingrese el importe que hubo en la sucursal {}, el dia {}", i,j))

def principal():
    arreglo_ventas=GestorVenta()
    arreglo_ventas.test()
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            d1=int(input("Ingresa el dia(1 a 7): "))
            n1=int(input("Ingresa la sucursal(1 a 5): "))
            i1=float(input("Ingresa el importe: "))
            arreglo_ventas.opcion1(d1,n1,i1)
        elif opcion==2:
            n2=int(input("Ingresa numero de sucursal: "))
            arreglo_ventas.opcion2(n2)
        elif opcion==3:
            d3=int(input("Ingresa el dia: "))
            arreglo_ventas.opcion3(d3)
        elif opcion==4:
            arreglo_ventas.opcion4()
        elif opcion==5:
            arreglo_ventas.opcion5()
        else:
            print("Opcion no valida")
        opcion=menu()

if  __name__ =='__main__':
    principal()