from .constructor_excel_clases import ConstructorExcel as Cons
import pandas as pd
import os

class LectorExcel(Cons):
    def __init__(self, archivo_excel):
        super().__init__(archivo_excel)

    def leer_excel(self,nombre_hoja):
        df = pd.read_excel(self.archivo_excel, sheet_name=nombre_hoja)
        return df
     
    def leer_hojas(self): 
        hojas = pd.ExcelFile(self.archivo_excel)
        return hojas.sheet_names

    def leer_columna(self,hoja,nombre_columna):
        df = self.leer_excel(hoja)
        datos_columna = df[nombre_columna]
        return datos_columna
    
    @property
    def nombre_archivo(self):
        nombre_archivo = os.path.splitext(os.path.basename(self.archivo_excel))[0]
        return nombre_archivo
    