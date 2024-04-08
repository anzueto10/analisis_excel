from abc import ABC, abstractmethod

class ConstructorExcel(ABC):
    @abstractmethod
    def __init__(self,archivo_excel):
        self.archivo_excel = archivo_excel
