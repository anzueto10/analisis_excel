from .estadisticas_excel import EstadisticasExcel as Estadisticas
import matplotlib.pyplot as plt
import seaborn as sns

class GraficoDeBarras(Estadisticas):
    def __init__(self, archivo_excel, nombre_hoja):
        super().__init__(archivo_excel, nombre_hoja)
    
    def generar_grafico(self,nombre_columna, titulo_grafico):
        #Generar la gráfica
        x = ["Promedio","Mediana", "Desviación Estándar"]
        y = [self.promedio(nombre_columna), self.mediana(nombre_columna), self.desviacion_estandar(nombre_columna)]

        plt.figure(figsize=(8, 6))
        sns.barplot(x=x, y=y, palette="viridis")

        # Añadir etiquetas y título
        plt.ylabel('Valores')
        plt.title(titulo_grafico)

        # Mostrar el gráfico
        plt.show()
    