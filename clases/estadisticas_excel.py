from lector_excel import LectorExcel as Lector

class EstadisticasExcel(Lector):
    def __init__(self,archivo_excel,nombre_hoja,promedio, mediana, desviacion_estandar, nombre_columna):
        super.__init__(archivo_excel,nombre_hoja)
        self.promedio = promedio
        self.mediana = mediana
        self.desviacion_estandar = desviacion_estandar
        self.nombre_columna = nombre_columna
    def leer_datos(self): pass

    def obtener_encabezados(self): pass
    
    def calcular_promedio(self, nombre_columna):pass
        
    def calcular_mediana(self, nombre_columna):pass
        
    def calcular_desviacion_estandar(self, nombre_columna): pass
            