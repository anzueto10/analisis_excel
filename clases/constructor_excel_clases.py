from abc import ABC, abstractmethod

class ConstructorExcel(ABC):
    @abstractmethod
    def __init__(self,archivo_excel,nombre_hoja):
        self.archivo_excel = archivo_excel
        self.nombre_hoja = nombre_hoja
