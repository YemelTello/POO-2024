from clasePublicacion import Publicacion

class CD(Publicacion):
    __tiempo: int
    __narrador: str

    def __init__(self, **kwargs):
        super().__init__(kwargs["tit"], kwargs["cat"], kwargs["pr"])
        self.__tiempo = kwargs["time"]
        self.__narrador = kwargs["narra"]

    def __str__(self):
        return f"Titulo: {super().getTitulo()}\n -> Tiempo de Reproduccion: {self.getTime()}"
    
    def getTime(self):
        return self.__tiempo
    
    def getNarrador(self):
        self.__narrador

    def getImporte(self):
        importe = float(self.getPrecioBase() + (10*self.getPrecioBase()) / 100)
        return importe