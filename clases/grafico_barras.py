from estadisticas_excel import EstadisticasExcel as Estadisticas

class GraficoDeBarras(Estadisticas):
    def __init__(self, archivo_excel, nombre_hoja, promedio, mediana, desviacion_estandar,nombre_columna,titulo_grafico):
        super().__init__(archivo_excel, nombre_hoja, promedio, mediana, desviacion_estandar,nombre_columna)
        self.titulo_grafico = titulo_grafico
        
    def leer_datos(self): pass

    def obtener_encabezados(self): pass
    
    def generar_grafico(self, nombre_columna, titulo_grafico): pass

    