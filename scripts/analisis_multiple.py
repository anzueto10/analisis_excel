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

#Definimos todas las funciones:--

#Esta es para obtener el archivo excel, basicamente agarra la ruta ya sí
def obtener_archivos_excel():
    carpeta = os.path.join(os.path.dirname(__file__), '..', 'data')
    archivos = os.listdir(carpeta)
    return archivos

#Este es para crear el informe o sea el archivo txt
def crear_informe(nombre_archivo,contenido):
    carpeta = os.path.join(os.path.dirname(__file__), '..', 'informes')
    ruta_archivo = os.path.join(carpeta, nombre_archivo)
    with open(ruta_archivo, "w", encoding='utf-8') as archivo:
    # Escribir el contenido en el archivo
        archivo.write(contenido)

#Este es para generar el grafico de barras      
def crear_grafico_de_barras(archivo_excel,nombre_hoja,nombre_columna,titulo_grafico):
    grafico_barras = GraficoDeBarras(archivo_excel,nombre_hoja)
    grafico_barras.generar_grafico(nombre_columna,titulo_grafico)

#Este es para obtener las estadtidscitcas
def obtener_estadisticas(archivo_excel,nombre_hoja,nombre_columna):
    estadisticas = EstadisticasExcel(archivo_excel,nombre_hoja)
    return estadisticas.promedio(nombre_columna), estadisticas.mediana(nombre_columna), estadisticas.desviacion_estandar(nombre_columna)

#Este es para obtener las columnas y los datos (Aunque ni lo usé)
def obtener_columnas_datos(archivo_excel,nombre_hoja):
    columnas_datos = ColumnasDatos(archivo_excel,nombre_hoja)
    return columnas_datos.datos, columnas_datos.encabezados

#Este es para obtener las hojas de u narchivo excel
def obtener_hojas(archivo_excel): 
    lector_excel = LectorExcel(archivo_excel,0)
    return lector_excel.leer_hojas()

#Y este es ya para unir todo y analizar el archivo 
def analizar_archivo_excel():
    #Acá lo que hacemos es primero, obtener todos los archivos posibles de la carpeta data
    archivos_excel = obtener_archivos_excel()
    #Luego, obtenemos su path así en carpeta
    carpeta_datos = os.path.join(os.path.dirname(__file__), '..', 'data')

    #Después, iniciamos un bucle for para poder analizar archivo por archivo
    for archivo in enumerate(archivos_excel):
        #Acá lo que hacemos es juntar el nombre del archivo con la ruta para que las calses puedan encontrarlo
        ruta_archivo = os.path.join(carpeta_datos, archivo[1])
        #Acá, mandamos a llamar la funsión de obtener hojas para obtener el número de hojas y sus nombres
        hojas = obtener_hojas(ruta_archivo)
        #Acá son los encabezados de los informes
        contenido = f"""---------------------------------------------
            Archivo: {archivo[1]}
            Número de hojas: {len(hojas)}
        """
        #Declaramos una variable para poder almacenar el contenido de cada hoja y ponerla en el informe
        contenido_hoja = ""
        #Iniciamos un bucle for para analizar cuantas hojas teenga el archivo, o sea, primero hacemos 
        #un bucle for para poder agarrar cuantos archivos haya, y de esos archivos, cuiantas hojas tengan
        for hoja in enumerate(hojas):
            #Aquí esto lo que hace es armar la estructura para luego ponerla en el informe.txt
            contenido_hoja += f"""   
            ---Hoja: {hoja[0] +1}
                
                *Estadísticas numéricas*
                
                Promedio: {obtener_estadisticas(ruta_archivo,hoja[1],"Total")[0]}
                Mediana: {obtener_estadisticas(ruta_archivo,hoja[1],"Total")[1]}
                Desviación Estándar: {obtener_estadisticas(ruta_archivo,hoja[1],"Total")[2]}
            """
            #Acá lo que hacemos es llamar a las funciones y mandarles, el archivo(bueno es su ruta pero bueno ya sabe), el número de hoja
            #que es dinámico, y el Total, psue total porque es la única columna numérica, y lo desempaqueatamos
            
            #Media vez, el archivo ya no tenga ojas por analizar, uniumos el encabezado junto con los contenidos de cada hoja
        contenido_final = f"""
{contenido}
{contenido_hoja}
--------------------------------------------------------
        """
        #Y creamos el informe, todo lo anterior se repite tantas veces como archivos existan
        crear_informe(f"informe_archivo{archivo[0]}.txt",contenido_final)
        #Y acá generamos el gráfico de barras
        crear_grafico_de_barras(ruta_archivo,hoja[1],"Total",f"Grafico de {archivo[1]}")
    

        