class Transacciones:
    __CVU: str
    __NumeroDeTransacción: str
    __Importe: float
    __TipodeTransacción: str

    def __init__(self, cvu, numero, importe, tipo):
        self.__CVU = cvu
        self.__NumeroDeTransacción = numero
        self.__Importe = importe
        self.__TipodeTransacción = tipo

    def getCVUt(self):
        #Retorna el numero de CVU
        return self.__CVU
    
    def getNumeroDeTransacción(self):
        #Retorna numero de transacción
        return self.__NumeroDeTransacción
    
    def getImporte(self):
        #Retorna el importe a pagar
        return self.__Importe

    def getTipoDeTransacción(self):
        #Retorna el tipo de transacción debito
        return self.__TipodeTransacción