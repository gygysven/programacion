# dnd implementarse o trabajar este proyecto
# examen tkiner (teorico y práctico)
# Elaborar un gestión de inventarios (stock) de productos adontologicos:
# - kinter, SQLite3, Copilot, Gemini, DeepSeek, etc.

import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import ttk
import uuid


# /// SQLite3
conexion = sqlite3.connect("inv_odonto.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        caregoria TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL
    )
""")

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.codigo = self.generar_codigo()
        self.precio = precio

    def generar_codigo(self):
        return str(uuid.uuid4())[:8]
    
    def registrar_venta(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            return False

def agregar_productos(nombre, categoria, cantidad, precio):
    conexion = sqlite3.connect("inv_odonto.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, caregoria, cantidad, precio) VALUES (?, ?, ?)",
                    nombre, categoria, cantidad, precio)

def mostrar_productos():
    conexion = sqlite3.connect("inv_odonto.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    print("Productos en el inventario:")
    for nombre, cantidad, precio in productos:
        print(f" - {nombre} (): {cantidad} unidades | Precio: {precio} soles")
    conexion.close()

def eliminar_producto(nombre):
    conexion = sqlite3.connect("inv_odonto.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE nombre = ?", (nombre,))
    conexion.commit()
    conexion.close()
    print(f"Producto '{nombre}' se eliminó correctamente.")

def buscar_producto(nombre):
    conexion = sqlite3.connect("inv_odonto.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
    producto = cursor.fetchone()
    if producto:
        print(f"Producto encontrado: {producto}")
    else:
        print(f"Producto '{nombre}' no encontrado.")
    
    cursor.execute("SELECT * FROM productos WHERE id = ?", (nombre,))
    conexion.close()

def ver_inventario():
    conexion = sqlite3.connect("inv_odonto.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    print("Inventario completo:")
    for producto in productos:
        print(producto)
    conexion.close()



ventana = tk.Tk()
ventana.title("Inventario de Productos Odontológicos")
ventana.geometry("600x400")
ventana.resizable(0, 0)
ventana.config(bg="lightblue")

frame = tk.Frame(ventana)
frame.pack(pady=20)

label_nombre = tk.Label(frame, text="Nombre:")  
label_nombre.grid(row=0, column=0, padx=5, pady=5)

# PLACEHOLDER

# def desaparece_placeholder(event):
#     if entry_nombre.get()== "Ingrese el nombre del producto":
#         entry_nombre.delete(0, tk.END)
#         entry_nombre.config(fg="white")

# def aparece_placeholder(event):
#     if entry_nombre.get()== "":
#         entry_nombre.delete(0, tk.END)
#         entry_nombre.config(fg="gray")

entry_nombre = tk.Entry(frame, fg="gray")
entry_nombre.grid(row=0, column=1, padx=5, pady=5)
entry_nombre.insert(0, "Ingrese nombre del producto")
# entry_nombre.bind("<FocusIn>", desaparece_placeholder)
# entry_nombre.bind("<FocusOut>", aparece_placeholder)
entry_nombre.focus()


label_categoria = tk.Label(frame, text="Categoría:")
label_categoria.grid(row=1, column=0, padx=5, pady=5)

combo_categoria = ttk.Combobox(frame, values=["Consumibles dentales", "Materiales dentales", "Instrumental odontológico", "Equipos odontológicos"], state="readonly", width=30)
combo_categoria.grid(row=1, column=1, padx=5, pady=5)
combo_categoria.insert(0, "Seleccione categoría")



ventana.mainloop()