from abc import ABC


class herenciaAños(ABC):
    _edadAFuturo = int(0)

    @staticmethod
    def cacularEdadAFuturo():
        pass

    def getEdadAFuturo(self):
        return self._edadAFuturo


class tiempoFuturo (herenciaAños):
    __años = int(0)
    __edadActual = int(0)

    def __init__(self, edadActual, años):
        self.__años = años
        self.__edadActual = edadActual
        self.calcularEdadAFuturo()

    def calcularEdadAFuturo(self):
        self._edadAFuturo = self.__edadActual + self.__años