#Importamos la librería para interfaces gráficas
from tkinter import *
import pyautogui


raiz = Tk()

raiz.title("Analizador de archivos excel :)")
raiz.resizable(False,False)
raiz.iconbitmap("logo.ico")

def obtener_size_screen():
    ancho_pantalla = raiz.winfo_screenwidth()
    alto_pantalla = raiz.winfo_screenheight()
    ancho_ventana = ancho_pantalla
    barra_tareas = pyautogui.size()[1] - ancho_pantalla
    alto_ventana = alto_pantalla - barra_tareas
    return ancho_ventana, alto_ventana

ventana_size = obtener_size_screen()
raiz.config(border=20,background="#fff")
raiz.geometry(f"1000x700")
raiz.mainloop()