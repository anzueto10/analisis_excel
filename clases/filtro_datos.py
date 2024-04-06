from .lector_excel import LectorExcel as Lector

class FiltroDatos(Lector):
    def __init__(self, archivo_excel,nombre_hoja):
        super().__init__(archivo_excel,nombre_hoja)
    
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