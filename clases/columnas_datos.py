from .lector_excel import LectorExcel as Lector

class ColumnasDatos(Lector):
    def __init__(self, archivo_excel, nombre_hoja):
        super().__init__(archivo_excel, nombre_hoja)
    
    @property
    def datos(self): 
        df = self.leer_excel()
        data = []
        for columna in df:
            datos_columna = df[columna]
            lista_columna = [columna] + datos_columna.tolist()
            # Agregar la lista a la lista de datos
            data.append(lista_columna)
        return data
    
    @property
    def encabezados(self):
        df = self.leer_excel()
        encabezados = df.columns.tolist()
        return encabezados