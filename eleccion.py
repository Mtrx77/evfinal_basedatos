import os
import subprocess
from tkinter import Tk, Label, Button, messagebox

def inscribir_alumno():
        ventana.destroy()
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        nombre_script = "inscribir.py"
        ruta_script = os.path.join(ruta_actual, nombre_script)
        subprocess.call(["python", ruta_script])

def consultar_alumno():
        ventana.destroy()
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        nombre_script = "consulta.py"
        ruta_script = os.path.join(ruta_actual, nombre_script)
        subprocess.call(["python", ruta_script])


ventana = Tk()
ventana.title("Menú")
ventana.geometry("300x200")

label_bienvenida = Label(ventana, text="¡Bienvenido! ¿Qué deseas hacer?")
label_bienvenida.pack(pady=20)

btn_inscribir = Button(ventana, text="Inscribir alumno", command=inscribir_alumno)
btn_inscribir.pack()

btn_consultar = Button(ventana, text="Consultar alumno", command=consultar_alumno)
btn_consultar.pack()

ventana.mainloop()
