#Importamos la librería para interfaces gráficas
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
    if archivo:
        print(f"Archivo seleccionado: {archivo}")
        
        
raiz = Tk()
raiz.title("Analizar Archivos Excel")
raiz.config(bg="#f0f0f0")
raiz.state('zoomed')
raiz.iconbitmap("logo.ico")

marco_principal = Frame(raiz, bg="#f0f0f0")
marco_principal.pack(expand=True, fill="both", padx=20, pady=20)

fuente_titulo = ("Calibri", 24, "bold")
titulo = Label(marco_principal, text="Analizador de tablas Excel", font=fuente_titulo, bg="#f0f0f0")
titulo.pack(pady=(0, 20))

s = ttk.Style()
s.configure(
    "Obtener_archivos.TButton", 
    foreground="#000",
    padding=(10,10),
    font=("Calibri", 18))

s.map("Obtener_archivos.TButton", bg=[("active", "#f0f0f0")])


boton_seleccionar_archivo = ttk.Button(marco_principal,command=seleccionar_archivo,text="Seleccionar archivo", style="Obtener_archivos.TButton")
boton_seleccionar_archivo.pack()

raiz.mainloop()