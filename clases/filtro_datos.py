from .lector_excel import LectorExcel as Lector
import pandas as pd

class FiltroDatos(Lector):
    def __init__(self, archivo_excel, nombre_hoja,valor_buscado):
        super().__init__(archivo_excel, nombre_hoja)
        self.valor_buscado = valor_buscado
        
    def leer_datos(self): pass
    
    def obtener_encabezados(self): pass
    
    def filtrar_por_valor(self, nombre_columna, valor_buscado): pass