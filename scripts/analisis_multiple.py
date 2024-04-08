import sys
import os
#Para las clases que luego me tira error
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
#Importamos lass clases
from clases.lector_excel import LectorExcel
from clases.estadisticas_excel import EstadisticasExcel
from clases.grafico_barras import GraficoDeBarras
from clases.filtro_datos import FiltroDatos
from clases.columnas_datos import ColumnasDatos
from clases.informe_estructura import InformeEstructura

#Definimos todas las funciones:--
class AnalisisMultiple():
    def __init__(self,archivo_excel):
        self.archivo_excel = archivo_excel
    
    #def obtener_archivos_excel():
       # carpeta = os.path.join(os.path.dirname(__file__), '..', 'data')
        #archivos = os.listdir(carpeta)
       # return archivos
    def obtener_nombre_archivo(self,archivo):
        leer_excel = LectorExcel(archivo)
        return leer_excel.nombre_archivo
    
    #Este es para crear el informe o sea el archivo txt
    def crear_informe(self):
        data_informe = InformeEstructura(self.archivo_excel)
        nombre_archivo = LectorExcel(self.archivo_excel).nombre_archivo
        encabezado_de_informe = data_informe.contenido_informe_encabezado
        contenido_hojas = data_informe.contenido_informe_hoja
        contenido = f"{encabezado_de_informe}\n{contenido_hojas}"
        #Acá obtenemos el nombre del achivo
        
        nombre_archivo = os.path.splitext(os.path.basename(self.archivo_excel))[0]
        #Carpeta donde se guardan los informes
        carpeta = os.path.join(os.path.dirname(__file__), '..', 'informes')
        ruta_archivo = os.path.join(carpeta,f"{nombre_archivo}.txt")
        with open(ruta_archivo, "w", encoding='utf-8') as archivo:
        # Escribir el contenido en el archivo
            archivo.write(contenido)

    #Este es para generar el grafico de barras      
    def crear_grafico_de_barras(self,nombre_hoja,nombre_columna,titulo_grafico):
        grafico_barras = GraficoDeBarras(self.archivo_excel)
        grafico_barras.generar_grafico(nombre_hoja,nombre_columna,titulo_grafico)

    #Este es para obtener las estadtidscitcas
    def obtener_estadisticas(self,nombre_hoja,nombre_columna):
        estadisticas = EstadisticasExcel(self.archivo_excel)
        return estadisticas.promedio(nombre_hoja,nombre_columna), estadisticas.mediana(nombre_hoja,nombre_columna), estadisticas.desviacion_estandar(nombre_hoja,nombre_columna)

    #Este es para obtener las columnas 
    def obtener_columnas_encabezados(self,nombre_hoja): return ColumnasDatos(self.archivo_excel).encabezados(nombre_hoja)

    #Este es para obtener las hojas de u narchivo excel
    def obtener_hojas(self): 
        lector_excel = LectorExcel(self.archivo_excel)
        return lector_excel.leer_hojas()
    
    #Este es para filtrar los datos de la hoja
    def filtrar_datos(self): pass
    
    def filtrar_numerica(self,hoja,columna):
        filtro = FiltroDatos(self.archivo_excel)
        columnas_numericas = filtro.filtrar_columnas_numericas(hoja,True)
        if columna in columnas_numericas: return True
        else: return False
        

        
    

        