from .lector_excel import LectorExcel as Lector
import pandas as pd

class EstadisticasExcel(Lector):
    def __init__(self,archivo_excel,nombre_hoja,nombre_columna ):
        super().__init__(archivo_excel,nombre_hoja)
        self.nombre_columna = nombre_columna
        
    def leer_datos(self):
        df = pd.read_excel(self.archivo_excel, sheet_name=self.nombre_hoja)
        data = []
        print(df[self.nombre_columna])
            
        
    def obtener_encabezados(self): pass
    
    def promedio(self, nombre_columna):        
        #Aquí definimos el data fream, leyendo con pandas el archivo que se envía desde el script
        df = pd.read_excel(self.archivo_excel, sheet_name=self.nombre_hoja)
        columna = df[nombre_columna]
        promedio = columna.mean()
        return promedio
    
    def mediana(self, nombre_columna):
        #Aquí definimos el data fream, leyendo con pandas el archivo que se envía desde el script
        df = pd.read_excel(self.archivo_excel, sheet_name=self.nombre_hoja)
        columna = df[nombre_columna]
        promedio = columna.median()
        return promedio
    
    def desviacion_estandar(self, nombre_columna): 
        #Aquí definimos el data fream, leyendo con pandas el archivo que se envía desde el script
        df = pd.read_excel(self.archivo_excel, sheet_name=self.nombre_hoja)
        columna = df[nombre_columna]
        promedio = columna.std()
        return promedio
            