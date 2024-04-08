from .lector_excel import LectorExcel as Lector

class ColumnasDatos(Lector):
    def __init__(self, archivo_excel):
        super().__init__(archivo_excel)
    
    
    def encabezados(self,hoja):
        df = self.leer_excel(hoja)
        encabezados = df.columns.tolist()
        return encabezados
    
    def numero_columna(self,hoja,nombre):
        df = self.leer_excel(hoja)
        numero_columna = df.columns.get_loc(nombre)
        return numero_columna