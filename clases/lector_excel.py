from .constructor_excel_clases import ConstructorExcel as Cons
import pandas as pd

class LectorExcel(Cons):
    def __init__(self, archivo_excel, nombre_hoja):
        super().__init__(archivo_excel, nombre_hoja)

    def leer_excel(self):
        df = pd.read_excel(self.archivo_excel, sheet_name=self.nombre_hoja)
        return df
     
    def leer_hojas(self): 
        hojas = pd.ExcelFile(self.archivo_excel)
        return hojas.sheet_names
        
        