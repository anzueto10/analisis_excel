#Importamos la librería para interfaces gráficas
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#Importamos el script
import scripts.analisis_multiple as anm
estadisticas_generadas = False

def generar_opciones_de_usuario(archivo):
    s = ttk.Style()
    s.configure(
        "opciones_usuario.TButton", 
        foreground="#000",
        bg="#fff",
        font=("Calibri", 18),
        padding=(29,20)
    )
    
    boton_obtener_datos = ttk.Button(contenedor_opciones_usuario,
                                     command=lambda:boton_obtener_datos_funsion(archivo),
                                     text="Obtener los datos en forma de tabla",
                                     style="opciones_usuario.TButton")
    boton_obtener_datos.pack(side="left",expand=True)
    
    boton_estadisticas = ttk.Button(contenedor_opciones_usuario, 
                                command=lambda:boton_estadisticas_funcion(archivo),
                                text="Generar Estadísticas de la hoja", 
                                style="opciones_usuario.TButton")
    boton_estadisticas.pack(side="left",expand=True)

    boton_generar_informe = ttk.Button(contenedor_opciones_usuario, 
                                   command=lambda: boton_informe_funcion(archivo),
                                   text="Generar un informe de la hoja", 
                                   style="opciones_usuario.TButton")
    boton_generar_informe.pack(side="left",expand=True)

    boton_generar_grafico_barras = ttk.Button(contenedor_opciones_usuario, 
                                           command=lambda: boton_grafica_funcion(archivo),
                                           text="Generar un gráfico de las estadísticas", 
                                           style="opciones_usuario.TButton")
    boton_generar_grafico_barras.pack(side="left",expand=True)

def boton_obtener_datos_funsion(archivo):
    hoja = hojas_ventana_emergente(archivo)
    mostrar_datos_en_tabla(archivo,hoja)
    
def obtener_datos_y_encabezados(archivo,hoja):
    analisis = anm.AnalisisMultiple(archivo)
    encabezados = analisis.obtener_columnas_encabezados(hoja)
    datos = analisis.obtener_datos_hoja(hoja)
    return encabezados,datos

def crear_tabla_datos(archivo,hoja,contenedor):
    encabezados, datos = obtener_datos_y_encabezados(archivo,hoja)
    
    datos = list(zip(*datos))

    #Crear tabla con encabezados y datos
    tabla_contenedor = ttk.Treeview(contenedor)
    tabla_contenedor["columns"] = encabezados

    for encabezado in encabezados:
        tabla_contenedor.heading(encabezado, text=encabezado)

    #Agregar datos a la tabla
    for fila in datos:
        tabla_contenedor.insert("", "end", values=fila)

    tabla_contenedor.pack(expand=True, fill="both")
    
def mostrar_datos_en_tabla(archivo,hoja):
    contenedor_tabla = Frame(marco_principal,bg="#fff")
    contenedor_tabla.pack(expand=True, fill="both", padx=5, pady=5)
    crear_tabla_datos(archivo,hoja,contenedor_tabla)
    
    
def generar_estadisticas(archivo):
    hoja = hojas_ventana_emergente(archivo)
    columna = columna_ventana_emergente(archivo,hoja)
    if columna != None:
        datos = obtener_estadisticas(archivo,hoja,columna)
        mostrar_datos_estadistica(datos,hoja,columna)
        global estadisticas_generadas
        estadisticas_generadas = True
    else: pass
    
def mostrar_datos_estadistica(datos,hoja,columna):
    contenedor_labels_estadistica = Frame(marco_principal, bg="#fff")
    contenedor_labels_estadistica.pack(expand=True, fill="both", padx=20, pady=20)

    s = ttk.Style()
    s.configure(
        "Texto.TLabel",
        font=("Calibri", 18),
        foreground="#000",
        bg="#fff",
        
    )
    
    s = ttk.Style()
    s.configure(
        "Titulo_contenedor_estadistica.TLabel",
        font=("Calibri", 22),
        foreground="#000",
    )
    
    titulo_de_contenedor = ttk.Label(contenedor_labels_estadistica,text=f"Datos estadísticos de {hoja}\nColumna: {columna}",style="Titulo_contenedor_estadistica.TLabel",anchor="center")
    titulo_de_contenedor.pack(side="top",expand=True)
    
    label_promedio = ttk.Label(contenedor_labels_estadistica, text=f"Promedio\n{datos[0]}", style="Texto.TLabel", anchor="center")
    label_promedio.pack(side="left", expand=True)

    label_mediana = ttk.Label(contenedor_labels_estadistica, text=f"Mediana\n{datos[1]}", style="Texto.TLabel", anchor="center")
    label_mediana.pack(side="left", expand=True)

    label_desviacion_estandar = ttk.Label(contenedor_labels_estadistica, text=f"Desviación Estándar\n{datos[2]}", style="Texto.TLabel", anchor="center")
    label_desviacion_estandar.pack(side="left", expand=True)
    

def boton_estadisticas_funcion(archivo):
    if not estadisticas_generadas:
        generar_estadisticas(archivo)
    else: pass
    
def boton_informe_funcion(archivo):generar_informe(archivo)

def boton_grafica_funcion(archivo):generar_grafica_barras(archivo)

def obtener_estadisticas(archivo,hoja,columna):
    analisis_columna = anm.AnalisisMultiple(archivo)
    promedio = analisis_columna.obtener_estadisticas(hoja,columna)[0]
    mediana = analisis_columna.obtener_estadisticas(hoja,columna)[1]
    desviacion_estandar = analisis_columna.obtener_estadisticas(hoja,columna)[2]
    return promedio,mediana,desviacion_estandar
    
def generar_informe(archivo):
    analisis = anm.AnalisisMultiple(archivo)
    analisis.crear_informe()
    informe_creado_ventana_emergente()
    
def generar_grafica_barras(archivo):
    hoja = hojas_ventana_emergente(archivo)
    columna = columna_ventana_emergente(archivo,hoja)
    if columna != None:
        titulo = obtener_titulo_del_grafico_ventana_emergente()
        analisis = anm.AnalisisMultiple(archivo)
        analisis.crear_grafico_de_barras(hoja,columna,titulo)
    else: pass
    
def obtener_data(archivo,hoja):
    analisis = anm.AnalisisMultiple(archivo)
    data = analisis.obtener_columnas_datos(hoja)
    return data
    
def obtener_hojas(archivo): 
    analisis = anm.AnalisisMultiple(archivo)
    hojas = analisis.obtener_hojas()
    return hojas
    
def obtener_columnas(archivo,hoja): 
    analisis = anm.AnalisisMultiple(archivo)
    columnas = analisis.obtener_columnas_encabezados(hoja)
    return columnas
 
def confirmar_columna_numerica(archivo,hoja,columna,ventana_actual):
    analisis = anm.AnalisisMultiple(archivo)
    es_numerica = analisis.filtrar_numerica(hoja,columna)
    if es_numerica: return True
    else: 
        error_ventana_emergente()
        ventana_actual.destroy()
        return False

def error_ventana_emergente():
    error_ventana = Toplevel(raiz)
    error_ventana.title("Error")
    error_ventana.config(padx=40,pady=40)
    
    contenedor_error = Frame(error_ventana, bg="#f0f0f0")
    contenedor_error.pack(expand=True, fill="both")
    
    s = ttk.Style()
    s.configure(
    "error_ventana.TLabel",
    font = ("Calibri", 24, "bold"),
    padding = ((0, 20)), 
    bg="#f0f0f0"
    ) 
    
    titulo_confirmacion = ttk.Label(contenedor_error,text="Tipo de columna no numérica, no puede ser analizada estadísticamente",style="error_ventana.TLabel")
    titulo_confirmacion.pack()
    
    s = ttk.Style()
    s.configure(
        "aceptar_error.TButton", 
        foreground="#000",
        padding=(10,10),
        font=("Calibri", 18))
    
    boton = ttk.Button(error_ventana, text=f"Aceptar", command=lambda: error_ventana.destroy(),style="aceptar_error.TButton")
    boton.pack()
    
    error_ventana.wait_window()

def hojas_ventana_emergente(archivo):
    confirmar_hoja_ventana = Toplevel(raiz)
    confirmar_hoja_ventana.title("Seleccione el número de hoja")
    confirmar_hoja_ventana.config(padx=40,pady=40)
    
    botones_contenedor = Frame(confirmar_hoja_ventana, bg="#f0f0f0")
    botones_contenedor.pack(expand=True, fill="both")
    
    s = ttk.Style()
    s.configure(
        "confirmar_hoja.TButton", 
        foreground="#000",
        padding=(10,10),
        font=("Calibri", 18))
    
    #Función para devolver el nombre de la hoja
    hoja_seleccionada = None  # Variable para almacenar la hoja seleccionada
    
    def enviar_hoja(hoja): 
        nonlocal hoja_seleccionada  # Acceder a la variable hoja_seleccionada no local
        confirmar_hoja_ventana.destroy()
        hoja_seleccionada = hoja
    
    numero_de_hojas = obtener_hojas(archivo)
    
    for i, hoja in enumerate(numero_de_hojas):
        boton = ttk.Button(botones_contenedor, text=f"Hoja{i+1}", command=lambda hoja=hoja: enviar_hoja(hoja),style="confirmar_hoja.TButton")
        boton.pack()
    
    confirmar_hoja_ventana.protocol("WM_DELETE_WINDOW", lambda: None)
    confirmar_hoja_ventana.wait_window()
    return hoja_seleccionada

def columna_ventana_emergente(archivo,hoja):
    confirmar_columna_ventana = Toplevel(raiz)
    confirmar_columna_ventana.title("Seleccione la columna a analizar")
    
    botones_contenedor = Frame(confirmar_columna_ventana, bg="#f0f0f0")
    botones_contenedor.pack(expand=True, fill="both", padx=20, pady=20)
    
    columnas = obtener_columnas(archivo,hoja)
    s = ttk.Style()
    s.configure(
        "confirmar_hoja.TButton", 
        foreground="#000",
        padding=(10,10),
        font=("Calibri", 18))
    
    #Función para devolver el nombre de la columna
    columna_seleccionada = None
    def enviar_columna(columna): 
        nonlocal columna_seleccionada
        confirmar_columna_ventana.destroy()
        valido = confirmar_columna_numerica(archivo,hoja,columna,confirmar_columna_ventana)
        if valido:columna_seleccionada = columna
        else: columna_seleccionada = None

    
    for columna in columnas:
        boton = ttk.Button(botones_contenedor, text=f"{columna}", command=lambda columna=columna:enviar_columna(columna),style="confirmar_hoja.TButton")
        boton.pack()
    
    confirmar_columna_ventana.protocol("WM_DELETE_WINDOW", lambda: None)
    confirmar_columna_ventana.wait_window()
    return columna_seleccionada

def obtener_titulo_del_grafico_ventana_emergente():
    nombre_de_grafico = Toplevel(raiz)
    nombre_de_grafico.title("Eliga un nombre para el gráfic")
    
    contenedor_input = Frame(nombre_de_grafico,bg="#f0f0f0")
    contenedor_input.pack(expand=True, fill="both", padx=20, pady=20)
    
    input_nombre_grafico = ttk.Entry(nombre_de_grafico)
    input_nombre_grafico.pack(padx=10, pady=10)
    titulo_grafico = ""
    def devolver_titulo_grafico():
        nonlocal titulo_grafico
        titulo_grafico = input_nombre_grafico.get()
        nombre_de_grafico.destroy()
        
    s = ttk.Style()
    s.configure(
        "confirmar_nombre.TButton", 
        foreground="#000",
        padding=(10,10),
        font=("Calibri", 18))
    
    boton_obtener_nombre = ttk.Button(contenedor_input, text="Guardar Nombre", command=lambda:devolver_titulo_grafico(),style="confirmar_nombre.TButton")
    boton_obtener_nombre.pack(pady=10)
    
    nombre_de_grafico.protocol("WM_DELETE_WINDOW", lambda: None)
    nombre_de_grafico.wait_window()
    return titulo_grafico

def informe_creado_ventana_emergente():
    confirmacion_ventana = Toplevel(raiz)
    confirmacion_ventana.title("Informe")
    
    contenedor_texto = Frame(confirmacion_ventana,bg="#f0f0f0")
    contenedor_texto.pack(expand=True, fill="both", padx=20, pady=20)
    s = ttk.Style()
    s.configure(
    "informe_creado_con_exito.TLabel",
    font = ("Calibri", 24, "bold"),
    padding = ((0, 20)), 
    bg="#f0f0f0"
    ) 
    
    titulo_confirmacion = ttk.Label(contenedor_texto,text="Informe creado con éxito",style="informe_creado_con_exito.TLabel")
    titulo_confirmacion.pack()
    
    s = ttk.Style()
    s.configure(
        "confirmar_informe_creado.TButton", 
        foreground="#000",
        padding=(10,10),
        font=("Calibri", 18))
    boton_aceptar_titulo_confirmacion = ttk.Button(contenedor_texto, text="Aceptar", command=lambda:confirmacion_ventana.destroy(),style="confirmar_informe_creado.TButton")
    boton_aceptar_titulo_confirmacion.pack()

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivo Excel", "*.xlsx;*.xls")])
    if archivo:
        borrar_frames(marco_principal)
        borrar_frames(contenedor_opciones_usuario)
        generar_opciones_de_usuario(archivo)
        global estadisticas_generadas
        estadisticas_generadas = False
        titulo.config(text=f"Analizar {anm.LectorExcel(archivo).nombre_archivo}")
        
def borrar_frames(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, Frame):
            widget.destroy()
        else:widget.destroy()
            
raiz = Tk()
raiz.title("Analizar Archivos Excel")
raiz.config(bg="#f0f0f0")
raiz.state('zoomed')
raiz.iconbitmap("logo.ico")

contenedor_archivo_y_titulo = Frame(raiz)
contenedor_archivo_y_titulo.pack(expand=True, fill="both", padx=20, pady=20)

s = ttk.Style()
s.configure(
    "Titulo_principal.TLabel",
    font = ("Calibri", 24, "bold"),
    padding = ((0, 20)), 
    bg="#f0f0f0"
    )

titulo = ttk.Label(contenedor_archivo_y_titulo, text=f"Analizador de tablas Excel",style="Titulo_principal.TLabel",anchor="center")
titulo.pack(side="top", expand=True, fill="both")

contenedor_opciones_usuario = Frame(raiz)
contenedor_opciones_usuario.pack(expand=True, fill="both", padx=20, pady=20)

marco_principal = Frame(raiz, bg="#f0f0f0")
marco_principal.pack(expand=True, fill="both", padx=20, pady=20)

s = ttk.Style()
s.configure(
    "Obtener_archivos.TButton", 
    foreground="#000",
    padding=(10,10),
    font=("Calibri", 18))

s.map("Obtener_archivos.TButton", bg=[("active", "#f0f0f0")])

boton_seleccionar_archivo = ttk.Button(contenedor_archivo_y_titulo,command=seleccionar_archivo,text="Seleccionar archivo", style="Obtener_archivos.TButton")
boton_seleccionar_archivo.pack(side="left",expand=True)

raiz.mainloop()