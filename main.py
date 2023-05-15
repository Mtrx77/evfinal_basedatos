import os
import json
import subprocess
from tkinter import messagebox, Tk, Label, Entry, Button, Frame
from pymongo import MongoClient

def login():

    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    try:
        client = MongoClient("mongodb+srv://" + usuario + ":" + contraseña + "@cluster0.d4aijtp.mongodb.net/")
        database_names = client.list_database_names()

        if database_names:
            datos = {
                "usuario": usuario,
                "contra": contraseña,
            }
            with open("datos.json", "w") as archivo:
                json.dump(datos, archivo)
            directorio_actual = os.path.dirname(os.path.abspath(__file__))
            ruta_archivo = os.path.join(directorio_actual, "datos.json")
            with open(ruta_archivo, "w") as archivo:
                json.dump(datos, archivo)    

            ventana.destroy()
            messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
            ruta_actual = os.path.dirname(os.path.abspath(__file__))
            nombre_script = "eleccion.py"
            ruta_script = os.path.join(ruta_actual, nombre_script)
            subprocess.call(["python", ruta_script])
        else:
            messagebox.showerror("Error", "Credenciales inválidas")
    except Exception as e:
        messagebox.showerror("Error", "Error al conectar a la base de datos: " + str(e))

ventana = Tk()
ventana.title("Login")
ventana.geometry("400x200")

marco = Frame(ventana, padx=20, pady=20)
marco.pack()

label_usuario = Label(marco, text="Usuario:", font=("Arial", 12))
label_usuario.grid(row=0, column=0, sticky="e", padx=5, pady=5)

label_contraseña = Label(marco, text="Contraseña:", font=("Arial", 12))
label_contraseña.grid(row=1, column=0, sticky="e", padx=5, pady=5)

entry_usuario = Entry(marco, font=("Arial", 12))
entry_usuario.grid(row=0, column=1, padx=5, pady=5)

entry_contraseña = Entry(marco, show="*", font=("Arial", 12))
entry_contraseña.grid(row=1, column=1, padx=5, pady=5)

btn_iniciar_sesion = Button(marco, text="Iniciar sesión", command=login, font=("Arial", 12))
btn_iniciar_sesion.grid(row=2, columnspan=2, pady=10)

ventana.mainloop()
