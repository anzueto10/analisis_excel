from .lector_excel import LectorExcel as Lector
from datetime import datetime
from pandas import Timestamp

class FiltroDatos(Lector):
    def __init__(self, archivo_excel):
        super().__init__(archivo_excel)
    
    def filtrar_por_valor(self,nombre_columna,valor_buscado):
        df = self.leer_excel()
        columna = df[nombre_columna]
        datos_encontrados = []
        #Hacemos un bucle para que busque lo datos en columna, si coincide con el criterio pues lo mete al array
        for i in columna:
            if i == valor_buscado:
                datos_encontrados.append(i)
                
        return datos_encontrados
    
    def filtrar_por_rango(self, nombre_columna, valor_minimo, valor_maximo):
        df = self.leer_excel()
        columna = df[nombre_columna]
        datos_encontrados = []
        #Acá igual hacemos otro bucle, si el valor es igual o menor que maximo y mayor o  igual que minimo, lo mete al array
        for i in columna:
            if i <= valor_maximo and i >= valor_minimo:
                datos_encontrados.append(i)
                
        return datos_encontrados
    
    def filtar_numericos(self,valor):
        try:
            int(valor)
            return True
        except ValueError: return False
        
    def filtrar_remover_fechas(self, valor):
        if isinstance(valor, Timestamp):
            return False  
        else:
            return True 
        
    def filtrar_fechas(self,valor):
        try:
            datetime.strptime(str(valor), '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False
        
    def filtrar_columnas_numericas(self,hoja,numerico_falso_verdadero):
        # Filtrar columnas numéricas
        df = self.leer_excel(hoja)
        columnas_numericas = df.select_dtypes(include=['number']).columns.tolist()
    
        # Filtrar columnas no numéricas
        columnas_no_numericas = df.columns.difference(columnas_numericas).tolist()
        
        if numerico_falso_verdadero: return columnas_numericas
        else: return columnas_no_numericas

    
