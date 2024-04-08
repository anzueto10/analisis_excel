from .estadisticas_excel import EstadisticasExcel as Estats
from .columnas_datos import ColumnasDatos as ColumData
from .filtro_datos import FiltroDatos as Filtro
from .datos_hoja import DatosHoja as Datos

class InformeEstructura(Estats,ColumData,Filtro,Datos):
    def __init__(self,archivo_excel):
        super().__init__(archivo_excel)
      
    @property  
    def contenido_informe_encabezado(self):
        encabezado = f"""---------------------------------------------
            Archivo: {self.archivo_excel}
            Número de hojas: {len(self.leer_hojas())}
        """
        return encabezado
        
    @property
    def contenido_informe_hoja(self):
        contenido_final = ""
        hojas = self.leer_hojas()
        
        for i,hoja in enumerate(hojas):
            contenido_por_hoja = ""
            contenido_por_hoja += f"""   
            ---Hoja: {i+1}
            Nombre de la hoja: {hoja}
            """
            
            contenido_columna = self.contenido_por_columna(hoja)
            contenido_final += f"{contenido_por_hoja}\n{contenido_columna}"
        return contenido_final
    
    def contenido_por_columna(self,hoja):
        contenido_por_columna = ""

        columnas_numericas = self.filtrar_columnas_numericas(hoja,True)
            
        for columna in columnas_numericas:
            numero_columna =  self.numero_columna(hoja,columna)
            contenido_por_columna+=f"""
            --Columna {numero_columna+1}
            Nombre de la columna: {columna}
            
            **Datos estadísticos**

                Promedio: {self.promedio(hoja,columna)}
                Mediana: {self.mediana(hoja,columna)}
                Desviación Estándar: {self.desviacion_estandar(hoja,columna)}
            """
        return contenido_por_columna