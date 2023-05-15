import json
import os
import subprocess
from pymongo import MongoClient
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox


with open("datos.json", "r") as archivo:
    datos = json.load(archivo)
usuario = datos["usuario"]
contraseña = datos["contra"]
client = MongoClient("mongodb+srv://" + usuario + ":" + contraseña + "@cluster0.d4aijtp.mongodb.net/")
if client:
    db = client["Base_Alumnos"]
    coleccion = db["Alumnos"]

def buscar_documento():
    valor_busqueda = entry_busqueda.get()
    resultado = coleccion.find_one({"Nombre": valor_busqueda})

    if resultado:
        resultado_texto.set("Documento encontrado:\n" + str(resultado))
    else:
        resultado_texto.set("No se encontró ningún documento que coincida con la búsqueda.")

def modificar_documento():
    valor_busqueda = entry_busqueda.get()
    resultado = coleccion.find_one({"Nombre": valor_busqueda})

    if resultado:
        resultado_texto.set("Documento encontrado:\n" + str(resultado))

        ventana_modificar = Tk()
        ventana_modificar.title("Modificar Usuario")
        ventana_modificar.geometry("400x200")

        label_modificacion = Label(ventana_modificar, text="Modificar atributos:")
        label_modificacion.pack()

        entry_nombre = Entry(ventana_modificar)
        entry_nombre.insert(0, resultado["Nombre"])
        entry_nombre.pack()

        entry_apellidos = Entry(ventana_modificar)
        entry_apellidos.insert(0, resultado["Apellidos"])
        entry_apellidos.pack()

        entry_fecha_nacimiento = Entry(ventana_modificar)
        entry_fecha_nacimiento.insert(0, resultado["Fecha de Nacimiento"])
        entry_fecha_nacimiento.pack()

        entry_carrera = Entry(ventana_modificar)
        entry_carrera.insert(0, resultado["Carrera"])
        entry_carrera.pack()
        def guardar_modificacion():
            nuevo_nombre = entry_nombre.get()
            nuevo_apellidos = entry_apellidos.get()
            nueva_fecha_nacimiento = entry_fecha_nacimiento.get()
            nueva_carrera = entry_carrera.get()

            resultado = coleccion.update_one({"Nombre": valor_busqueda},
                                             {"$set": {"Nombre": nuevo_nombre,
                                                       "Apellidos": nuevo_apellidos,
                                                       "Fecha de Nacimiento": nueva_fecha_nacimiento,
                                                       "Carrera": nueva_carrera}})

            ventana_modificar.destroy()

            messagebox.showinfo("Modificación exitosa", "El usuario ha sido modificado correctamente.")

        btn_guardar = Button(ventana_modificar, text="Guardar", command=guardar_modificacion)
        btn_guardar.pack()

        ventana_modificar.mainloop()
    else:
        resultado_texto.set("No se encontró ningún documento que coincida con la búsqueda.")

def eliminar_documento():
    valor_busqueda = entry_busqueda.get()
    confirmar = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro de que deseas eliminar el usuario?")

    if confirmar:
        resultado = coleccion.delete_one({"Nombre": valor_busqueda})

        if resultado.deleted_count > 0:
            resultado_texto.set("El usuario ha sido eliminado correctamente.")
        else:
            resultado_texto.set("No se encontró ningún documento que coincida con la búsqueda.")

def atras():
    ventana.destroy()
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    nombre_script = "eleccion.py"
    ruta_script = os.path.join(ruta_actual, nombre_script)
    subprocess.call(["python", ruta_script])

ventana = Tk()
ventana.title("Consultar")
ventana.geometry("400x200")

label_busqueda = Label(ventana, text="Consultar Alumno:")
label_busqueda.pack()
entry_busqueda = Entry(ventana)
entry_busqueda.pack()

btn_buscar = Button(ventana, text="Buscar", command=buscar_documento)
btn_buscar.pack()

btn_modificar = Button(ventana, text="Modificar", command=modificar_documento)
btn_modificar.pack()

btn_eliminar = Button(ventana, text="Eliminar", command=eliminar_documento)
btn_eliminar.pack()

resultado_texto = StringVar()
label_resultado = Label(ventana, textvariable=resultado_texto)
label_resultado.pack()


btn_atras = Button(ventana, text="Atrás", command=atras)
btn_atras.pack()


ventana.mainloop()
      