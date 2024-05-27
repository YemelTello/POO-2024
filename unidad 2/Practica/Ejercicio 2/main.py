from ClaseContenedor import CajaAhorro

def test():
    b = CajaAhorro
    Cuil = input("Ingrese cuil: ")
    b.ObtenerDatos(Cuil)
    b.AgregarDatos(Cuil)

if __name__ == '__main__':
    test()