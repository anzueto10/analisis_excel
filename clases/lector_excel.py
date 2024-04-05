from abc import ABC, abstractmethod

class LectorExcel(ABC):
    @abstractmethod
    def __init__(self,archivo_excel,nombre_hoja):
        self.archivo_excel = archivo_excel
        self.nombre_hoja = nombre_hoja
    
    @abstractmethod
    def leer_datos(self): pass
    
    @abstractmethod
    def obtener_encabezados(self): pass
        