import tkinter as tk
from tkinter import ttk, messagebox
import json
import uuid

# Sistema de logistica - sistema de inventario
# Caracteristica:
# - Eficiente
# - Amigable
# - La interfaz debe evitar errores humanos de data entry
# - Almacena los datos en una ruta dentro de la computadora (json)
# - Exporta el inventario a json y csv

# Consideraciones:
# -Usar Github copilot
# Utilizar tkinter

# pip install pyinstaller

class Producto:
    def __init__(self, nombre, stock, codigo, precio):
        self.nombre = nombre
        self.stock = stock
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
    carrito = []
def agregar_producto():
    productoSeleccionado = combo_productos.get()
    cantidadProductos = entry_cantidad.get()
    if productoSeleccionado == "" or cantidadProductos == "":
        messagebox.showwarning("Advertencia", "Por favor, seleccione un producto y una cantidad válida.")
        return
    else:
        cantidad = int(cantidadProductos)
        if cantidad <= 0:
            messagebox.showwarning("Advertencia", "La cantidad debe ser mayor a cero.")
            raise ValueError
            
        if cantidad > 0:
            precioUnitario = productos[productoSeleccionado].precio
            global subtotalProducto
            subtotalProducto = precioUnitario * cantidad
            carrito.append((productoSeleccionado, cantidad, subtotalProducto))
            listbox_carrito.insert(tk.END, f"{productoSeleccionado} x {cantidad} - S/ {subtotalProducto:.2f}")
            actualizar_totales()


# CREACIÓN DE VENTANA

ventana = tk.Tk()
ventana.title("Sistema de Electrónicos")
ventana.geometry("600x500")
ventana.resizable(False, False)
ventana.configure(bg="#f0f0f0")

frame = tk.Frame(ventana, padx=15, pady=15, bg="#f9f9f9")
frame.pack(expand=True, fill="both")

# -------------------------------

# REGISTRO DE PRODUCTOS
productos = {
    "Bluca": Producto("Laptop", 10, "precio", 2500.00),
    "Smartphone": Producto("Smartphone", 20,"precio", 1500.00),
    "Tablet": Producto("Tablet", 15,"precio", 1200.00),
    "Smartwatch": Producto("Smartwatch", 25,"precio", 800.00)
}

# -------------------------------

# INGRESO DE NÚMEROS

def validate_cantidad(char):
    if char == "":
        return True
    return char.isdigit()

# REGISTRO DE VENTAS

def agregar_al_carrito():
    tk.Label(frame, text="Seleccione producto:", bg="#f9f9f9", font=("Arial", 10, "bold")).pack(anchor="w")
    combo_productos = ttk.Combobox(frame, values=list(productos.keys()), state="readonly", width=30)
    combo_productos.pack(pady=5)

    btn_agregar = tk.Button(frame, text="Agregar al carrito", command=agregar_producto, bg="#4CAF50", fg="white", width=20)
    btn_agregar.pack(pady=5)

    tk.Label(frame, text="Cantidad:", bg="#f9f9f9", font=("Arial", 10, "bold")).pack(anchor="w")
    entry_cantidad = tk.Entry(frame, width=10)
    validate_command = ventana.register(validate_cantidad)
    
    entry = tk.Entry(frame, validate="key", validatecommand=(validate_command, "%S"))
    entry.pack(pady=10)

ventana.mainloop()