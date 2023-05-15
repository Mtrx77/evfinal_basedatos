import os
import subprocess
from tkinter import messagebox, Tk, Label, Entry, Button, Frame
from pymongo import MongoClient
import json

with open("datos.json", "r") as archivo:
    datos = json.load(archivo)
usuario = datos["usuario"]
contraseña = datos["contra"]
client = MongoClient("mongodb+srv://" + usuario + ":" + contraseña + "@cluster0.d4aijtp.mongodb.net/")
if client:
    db = client["Base_Alumnos"]
    coleccion = db["Alumnos"]
    carreras_validas = db["Carreras"].find()

    def validar_carrera():
        esvalido = False
        carrera = entry_carrera.get()

        for c in carreras_validas:
            if c["Carrera"] == carrera:
                esvalido = True
                break
        if esvalido == True:
            label_validacion.config(text="Carrera válida", fg="green")
            return True
        else:
            label_validacion.config(text="Carrera inválida", fg="red")
            return False

    def guardar_datos():
        if validar_carrera():
            nombre = entry_nombre.get()
            apellidos = entry_apellidos.get()
            fecha_nacimiento = entry_fecha_nacimiento.get()
            carrera = entry_carrera.get()
            documento = {"Nombre": nombre, "Apellidos": apellidos, "Fecha de Nacimiento": fecha_nacimiento, "Carrera": carrera}
            coleccion.insert_one(documento)
            label_estatus.config(text="Estatus: Inscrito", fg="green")
            ventana.after(3000, lambda: close_window_and_call_script())
    

    def close_window_and_call_script():
        ventana.destroy()
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        nombre_script = "eleccion.py"
        ruta_script = os.path.join(ruta_actual, nombre_script)
        subprocess.call(["python", ruta_script])

    def volver_atras():
        ventana.destroy()
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
        nombre_script = "eleccion.py"
        ruta_script = os.path.join(ruta_actual, nombre_script)
        subprocess.call(["python", ruta_script])


    ventana = Tk()
    ventana.title("Inscripcion")
    ventana.geometry("300x300")

    label_nombre = Label(ventana, text="Nombre:")
    label_nombre.pack()
    entry_nombre = Entry(ventana)
    entry_nombre.pack()

    label_apellidos = Label(ventana, text="Apellidos:")
    label_apellidos.pack()
    entry_apellidos = Entry(ventana)
    entry_apellidos.pack()

    label_fecha_nacimiento = Label(ventana, text="Fecha de Nacimiento:")
    label_fecha_nacimiento.pack()
    entry_fecha_nacimiento = Entry(ventana)
    entry_fecha_nacimiento.pack()

    label_carrera = Label(ventana, text="Carrera:")
    label_carrera.pack()
    entry_carrera = Entry(ventana)
    entry_carrera.pack()

    label_validacion = Label(ventana, text="")
    label_validacion.pack()

    label_estatus = Label(ventana, text="Estatus:")
    label_estatus.pack()
    label_estatus.config(text="Estatus: No inscrito", fg="Red")

    btn_guardar = Button(ventana, text="Guardar", command=guardar_datos)
    btn_guardar.pack()

    btn_atras = Button(ventana, text="Atrás", command=volver_atras)
    btn_atras.pack()

    ventana.mainloop()
