class CajaAhorro:
    __nroCuenta : str
    __cuil : str
    __apellido : str
    __nombre : str
    __saldo : float

    def __init__(self, nroCuenta, cuil, apellido, nombre, saldo):
        self.__nroCuenta = nroCuenta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = saldo

    def mostrarDatos(self):
        print("Nombre: {}, Apellido: {}, CUIL: {}, NROCUENTA: {}, SALDO: {}\n".format(self.__nombre,self.__apellido,self.__cuil,self.__nroCuenta,self.__saldo))
    
    def extraer(self, importe):
            if(importe<self.__saldo):
                self.__saldo -= importe
                print("el nuevo saldo es: ", self.__saldo)
            else:
                print("No puede sacar esa cantidad")

    def depositar(self, importe):
        if(importe>0):
            self.__saldo += importe
            print("El nuevo saldo es: ", self.__saldo)
        else:
            print("No puede ingresar esa cantidad")

    def validarCUIL(self):
        # Esta validacion no es perfecta. Si ingresamos un CUIL en el que originalmente XY era 20/27,
        # como 23; no sera capaz de detectar el error.
        lista=[]
        indice=(0,1,3,4,5,6,7,8,9,10) #Esta tupla contiene los indices de los digitos con los cuales se hara el producto
        constante=(5,4,3,2,7,6,5,4,3,2) #Esta tupla contiene las constantes que multiplicaran a los digitos
        acum=0
        for i in range(len(self.__cuil)-3): #El -3 se debe a los dos guiones(-) y al digito z; los cuales no se tienen en cuenta para realziar la operacion
            lista.append(int(self.__cuil[indice[i]])*constante[i])

        for i in lista:
            acum+=i
        p1=acum//11
        p2=acum-(p1*11)
        if p2==0:
            if self.__cuil[12]!='0':
                print('CUIL erroneo. El digito de verificacion deberia ser 0')
            else:
                print('El CUIL es valido')
        #Este bloque detecta CUILs cuyos digitos XY deberian ser 23, pues son repetidos
        elif p2==1:
            if self.__cuil[0:2]=='20':
                if self.__cuil[12]!='9':
                    print('CUIL invalido. Los digitos XY deberian tomar el valor 23, y Z el 9')
                else:
                    print('CUIL invalido. Los digitos XY deberian tomar el valor 23')
            elif self.__cuil[0:2]=='27':
                if self.__cuil[12]!='4':
                    print('CUIL invalido. Los digitos XY deberian tomar el valor 23, y Z el 4')
                else:
                    print('CUIL invalido. Los digitos XY deberian tomar el valor 23')
        else:
            band=False
            valido=('4','9')
            if self.__cuil[0:2]=='23':
                if (self.__cuil[12] in valido)is False:
                    print('CUIL invalido. Su digito de verificacion deberia ser 4 o 9')
                else:
                    band=True
            else:
                z=11-p2
                if int(self.__cuil[12])!=z:
                    print('CUIL invalido. Z deberia tomar el valor ',z)
                else:
                    band=True
            if band is True:
                print('CUIL valido')