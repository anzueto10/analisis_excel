from .lector_excel import LectorExcel as Leer

class DatosHoja(Leer):
    def __init__(self, archivo_excel):
        super().__init__(archivo_excel)
    
    def obtener_datos_con_encabezado(self,hoja): 
        df = self.leer_excel(hoja)
        data = []
        for columna in df:
            datos_columna = df[columna]
            lista_columna = [columna] + datos_columna.tolist()
            # Agregar la lista a la lista de datos
            data.append(lista_columna)
        return data
    
    def obtener_datos_sin_encabezado(self,hoja): 
        df = self.leer_excel(hoja)
        data = []
        for columna in df:
            datos_columna = df[columna]
            lista_columna = datos_columna.tolist()
            # Agregar la lista a la lista de datos
            data.append(lista_columna)
        return data