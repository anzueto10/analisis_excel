from .lector_excel import LectorExcel as Lector

class EstadisticasExcel(Lector):
    def __init__(self,archivo_excel,nombre_hoja):
        super().__init__(archivo_excel,nombre_hoja)
    
    def promedio(self,nombre_columna):        
        #Aquí definimos el data fream, leyendo con pandas el archivo que se envía desde el script
        df = self.leer_excel()
        columna = df[nombre_columna]
        #Calculamos el promedio con el método mean
        promedio = columna.mean()
        return promedio.round(2)
    
    def mediana(self,nombre_columna):
        #Aquí definimos el data fream, leyendo con pandas el archivo que se envía desde el script
        df = self.leer_excel()
        columna = df[nombre_columna]
        #Calculamos la mediana con el método median
        mediana = columna.median()
        return mediana.round(2)
     
    def desviacion_estandar(self,nombre_columna): 
        #Aquí definimos el data fream, leyendo con pandas el archivo que se envía desde el script
        df = self.leer_excel()
        columna = df[nombre_columna]
        #Calculamos la desviación estándar
        desviacion_estandar = columna.std()
        return desviacion_estandar.round(2)
            