import numpy as np

class GestorVenta:
    __arreglo: np.ndarray

    def __init__(self):
        self.__arreglo= np.empty([5,7],dtype=float)