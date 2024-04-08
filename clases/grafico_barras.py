from .estadisticas_excel import EstadisticasExcel as Estadisticas
import matplotlib.pyplot as plt
import seaborn as sns

class GraficoDeBarras(Estadisticas):
    def __init__(self, archivo_excel):
        super().__init__(archivo_excel)
    
    def generar_grafico(self,hoja,nombre_columna, titulo_grafico):
        #Generar la gráfica
        x = ["Promedio","Mediana", "Desviación Estándar"]
        y = [self.promedio(hoja,nombre_columna), self.mediana(hoja,nombre_columna), self.desviacion_estandar(hoja,nombre_columna)]

        plt.figure(figsize=(8, 6))
        sns.barplot(x=x, y=y, palette="viridis")

        # Añadir etiquetas y título
        plt.ylabel('Valores')
        plt.title(titulo_grafico)

        # Mostrar el gráfico
        plt.show()
    