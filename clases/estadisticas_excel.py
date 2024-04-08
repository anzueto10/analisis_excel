from .lector_excel import LectorExcel as Lector

class EstadisticasExcel(Lector):
    def __init__(self,archivo_excel):
        super().__init__(archivo_excel)
    
    def promedio(self,hoja,nombre_columna):        
        columna = self.leer_columna(hoja,nombre_columna)
        #Calculamos el promedio con el método mean
        promedio = columna.mean()
        return promedio.round(2)
    
    def mediana(self,hoja,nombre_columna):
        columna = self.leer_columna(hoja,nombre_columna)
        #Calculamos la mediana con el método median
        mediana = columna.median()
        return mediana.round(2)
     
    def desviacion_estandar(self,hoja,nombre_columna): 
        columna = self.leer_columna(hoja,nombre_columna)
        #Calculamos la desviación estándar
        desviacion_estandar = columna.std()
        return desviacion_estandar.round(2)
            