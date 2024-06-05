from clasePublicacion import Publicacion

class Libro(Publicacion):
    __nombreAutor: str
    __fechaEdicion: str
    __cantidadPags: int

    def __init__(self, **kwargs):
        super().__init__(kwargs["tit"], kwargs["cat"], kwargs["pr"])
        self.__nombreAutor = kwargs["nomb"]
        self.__fechaEdicion = kwargs["Fecha"]
        self.__cantidadPags = kwargs["cant"]

    def __str__(self):
        return f"Titulo: {super().getTitulo()}\n -> Autor: {self.getNombre()}"

    def getNombre(self):
        return self.__nombreAutor
    
    def getFecha(self):
        return self.__fechaEdicion
    
    def getCantidad(self):
        return self.__cantidadPags
    
    def getImporte(self):
        año = int(self.getFecha()[6:10])
        importe = float(self.getPrecioBase() - ((2024 - año) * self.getPrecioBase()) /100)
        return importe