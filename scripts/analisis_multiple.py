import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

sys.path.append(parent_dir)

from clases.estadisticas_excel import EstadisticasExcel
from clases.grafico_barras import GraficoDeBarras
from clases.filtro_datos import FiltroDatos

#Ruta para encontrar las tablas
archivo_excel =  os.path.join(os.path.dirname(__file__), '..', 'data', 'tablas_compras.xlsx')

analizar_estadistica = EstadisticasExcel(archivo_excel,"Compras Lunes", "Total")
analizar_estadistica.leer_datos()
promedio = analizar_estadistica.promedio("Total")
print(round(promedio,2))