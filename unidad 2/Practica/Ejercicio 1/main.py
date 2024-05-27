from claseCajaAhorro import CajaAhorro

def test():
        print("\nIngrese los siguientes datos: ")
        apellido = str(input("APELLIDO: "))
        nombre = str(input("NOMBRE: "))
        cuil = str(input("CUIL: "))
        nroCuenta = str(input("NUMERO DE CUENTA: "))
        saldo = float(input("SALDO: "))
        unaCuenta = CajaAhorro(nroCuenta, cuil, apellido, nombre, saldo)
        return unaCuenta

def cargaCuenta(lista):
       for i in range(3):
              C = test()
              lista.append(C)

if __name__ == '__main__':
    listaTest = []
    cargaCuenta(listaTest)
    for i in range(len(listaTest)):
            listaTest[i].mostrarDatos()
            importe = float(input("Ingresa cantidad que quiere extraer: "))
            listaTest[i].extraer(importe)
            Importe = float(input("CANTIDAD DE PLATA QUE QUIERE METER: "))
            listaTest[i].depositar(Importe)