class Reserva:
    __numero: int
    __cliente: str
    __numCabana: int
    __fecha: str
    __cantHuespe: int
    __cantDia: int
    __impSena: float

    def __init__(self, num, client, cabana, fecha, cantH, cantD ,sena):
        self.__numero = num
        self.__cliente = client
        self.__numCabana = cabana
        self.__fecha = fecha
        self.__cantHuespe = cantH
        self.__cantDia = cantD
        self.__impSena = sena
    
    def getNumR(self):
        #retorna el numero de reserva
        return self.__numero
    
    def getCliente(self):
        #retorna el nombre del cliente
        return self.__cliente
    
    def getCabana(self):
        #retorna el numero de la cabaña
        return self.__numCabana
    
    def getFecha(self):
        #retorna la fecha en que esta hecha la reserva
        return self.__fecha
    
    def getCantHuespe(self):
        #retorna la cantidad de huespedes que estan anotados en la reserva
        return self.__cantHuespe
    
    def getCantDia(self):
        #retorna la cantidad de dias que se van a hospedar
        return self.__cantDia
    
    def getImporte(self):
        #retorna la cantidad de importe que deben señar
        return self.__impSena
    
    def __str__(self):
        texto="Numero de Reserva {} Nombre de Huespes {} Numero de cabaña {} Fecha de Hospedaje {} Cantidad de huespedes {} Dias {} Importe de seña {}"
        return texto.format(self.__numero,self.__cliente.replace(',',''),self.__numCabana,self.__fecha,self.__cantHuespe,self.__cantDia,self.__impSena)