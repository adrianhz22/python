import customtkinter as ctk
from tkinter import Listbox, END
import json
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

CARPETA = "GUI"
ARCHIVO = os.path.join(CARPETA, "tareas.json")

os.makedirs(CARPETA, exist_ok=True)

def cargar_tareas():
    global tareas, completadas
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            data = json.load(f)
            tareas = data.get("tareas", [])
            completadas = data.get("completadas", [])
    else:
        tareas = ["Tender la ropa", "Hacer la comida", "Pasear al perro"]
        completadas = [False] * len(tareas)

def guardar_tareas():
    data = {
        "tareas": tareas,
        "completadas": completadas
    }
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def actualizar_lista():
    lista.delete(0, END)
    for i, tarea in enumerate(tareas):
        if completadas[i]:
            lista.insert(END, f"✔ {tarea}")
        else:
            lista.insert(END, tarea)
    guardar_tareas()

def añadir_tarea():
    tarea = entrada.get()
    if tarea.strip() != "":
        tareas.append(tarea)
        completadas.append(False)
        entrada.delete(0, END)
        actualizar_lista()

def eliminar_tarea():
    try:
        seleccion = lista.curselection()[0]
        tareas.pop(seleccion)
        completadas.pop(seleccion)
        actualizar_lista()
    except IndexError:
        pass

def toggle_completada(event):
    try:
        index = lista.curselection()[0]
        completadas[index] = not completadas[index]
        actualizar_lista()
    except IndexError:
        pass

cargar_tareas()

app = ctk.CTk()
app.title("Gestor de tareas")
app.geometry("500x500")

titulo = ctk.CTkLabel(app, text="Gestor de tareas", font=("Arial", 24, "bold"))
titulo.pack(pady=15)

frame_input = ctk.CTkFrame(app)
frame_input.pack(pady=10, padx=20, fill="x")

entrada = ctk.CTkEntry(frame_input, placeholder_text="Escribe una tarea...")
entrada.pack(side="left", padx=10, pady=10, fill="x", expand=True)

boton_add = ctk.CTkButton(frame_input, text="Añadir", command=añadir_tarea)
boton_add.pack(side="right", padx=10)

lista = Listbox(app, font=("Arial", 14))
lista.pack(padx=20, pady=10, fill="both", expand=True)
lista.bind("<Double-1>", toggle_completada)

boton_delete = ctk.CTkButton(app, text="Eliminar tarea seleccionada", fg_color="red", command=eliminar_tarea)
boton_delete.pack(pady=10)

actualizar_lista()

app.mainloop()