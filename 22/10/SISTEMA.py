# Completar la lógica de las funciones:
# agregar_producto()
# actualizar_totales()
# limpiar_carrito()
# finalizar_compra()
# Validar entradas (cantidad > 0, producto seleccionado).
# Calcular subtotales, IGV y total.
# Actualizar las etiquetas (label_subtotal, label_igv, label_total).
# Usar messagebox.showinfo para mostrar el resumen final.


import tkinter as tk
from tkinter import ttk, messagebox

# -------------------------------
# Datos iniciales
# -------------------------------

# Diccionario de productos con precios
productos = {
    "Arroz (S/ 5.00)": 5.00,
    "Azúcar (S/ 4.50)": 4.50,
    "Leche (S/ 3.20)": 3.20,
    "Pan (S/ 0.50)": 0.50,
    "Aceite (S/ 10.00)": 10.00
}

# Lista para guardar los productos agregados al carrito
carrito = []

# -------------------------------
# Funciones (a completar por los alumnos)
# -------------------------------

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
            precioUnitario = productos[productoSeleccionado]
            global subtotalProducto
            subtotalProducto = precioUnitario * cantidad
            carrito.append((productoSeleccionado, cantidad, subtotalProducto))
            listbox_carrito.insert(tk.END, f"{productoSeleccionado} x {cantidad} - S/ {subtotalProducto:.2f}")
            actualizar_totales()
    # TODO: Completar la lógica de validación, cálculo y agregado
    pass



def actualizar_totales():
    subtotal_list = [item[2] for item in carrito]
    subtotal = sum(subtotal_list)
    igv = subtotal * 0.18
    total = subtotal + igv
    label_subtotal.config(text=f"Subtotal: S/. {subtotal:.2f}")
    label_igv.config(text=f"IGV (18%): S/. {igv:.2f}")
    label_total.config(text=f"Total: S/. {total:.2f}")
    """Calcula y actualiza el subtotal, IGV (18%) y total a pagar."""
    # TODO: Completar cálculo de totales
    pass


def limpiar_carrito():
    carrito.clear()
    listbox_carrito.delete(0, tk.END)
    label_subtotal.config(text="Subtotal: S/. 0.00")
    label_igv.config(text="IGV (18%): S/. 0.00")
    label_total.config(text="Total: S/. 0.00")
    """Limpia el carrito y reinicia las etiquetas de totales."""
    # TODO: Limpiar lista y actualizar interfaz
    pass


def finalizar_compra():
    subtotal_list = [item[2] for item in carrito]
    subtotal = sum(subtotal_list)
    igv = subtotal * 0.18
    total = subtotal + igv
    pedido = [f"{item[0]} x {item[1]} - S/ {item[2]:.2f}" for item in carrito]
    resumen_texto= "\n=== RESUMEN DEL PEDIDO ===\n" + "\n".join(pedido) + f"\n\nSubtotal: S/{subtotal}" +f"\nIGV: S/{igv:.2f}\n" + f"\n\nTotal a pagar: S/{total:.2f}\n"
    messagebox.showinfo("Resumen de Compra", resumen_texto)
    """Muestra un resumen final con messagebox."""
    # TODO: Mostrar mensaje final con total a pagar
    pass


# -------------------------------
# Ventana principal
# -------------------------------

root = tk.Tk()
root.title("Mini Sistema de Ventas")
root.geometry("500x500")
root.resizable(False, False)

frame = tk.Frame(root, padx=15, pady=15, bg="#f9f9f9")
frame.pack(expand=True, fill="both")

# -------------------------------
# Sección de selección de producto
# -------------------------------
tk.Label(frame, text="Seleccione producto:", bg="#f9f9f9", font=("Arial", 10, "bold")).pack(anchor="w")
combo_productos = ttk.Combobox(frame, values=list(productos.keys()), state="readonly", width=30)
combo_productos.pack(pady=5)

tk.Label(frame, text="Cantidad:", bg="#f9f9f9", font=("Arial", 10, "bold")).pack(anchor="w")
entry_cantidad = tk.Entry(frame, width=10)
entry_cantidad.pack(pady=5)

btn_agregar = tk.Button(frame, text="Agregar al carrito", command=agregar_producto, bg="#4CAF50", fg="white", width=20)
btn_agregar.pack(pady=5)

# -------------------------------
# Carrito de compras
# -------------------------------
tk.Label(frame, text="Carrito de compras:", bg="#f9f9f9", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 0))
listbox_carrito = tk.Listbox(frame, width=50, height=10)
listbox_carrito.pack(pady=5)
listbox_carrito.insert(tk.END, )

# -------------------------------
# Totales
# -------------------------------
label_subtotal = tk.Label(frame, text=f"Subtotal: S/.", bg="#f9f9f9", font=("Arial", 10, "bold"))
label_subtotal.pack(anchor="w")
label_igv = tk.Label(frame, text="IGV (18%): S/ 0.00", bg="#f9f9f9", font=("Arial", 10, "bold"))
label_igv.pack(anchor="w")
label_total = tk.Label(frame, text="Total: S/ 0.00", bg="#f9f9f9", font=("Arial", 10, "bold"))
label_total.pack(anchor="w")

# -------------------------------
# Botones finales
# -------------------------------
btn_finalizar = tk.Button(frame, text="Finalizar compra", command=finalizar_compra, bg="#2196F3", fg="white", width=20)
btn_finalizar.pack(pady=10)

btn_limpiar = tk.Button(frame, text="Limpiar carrito", command=limpiar_carrito, bg="#f44336", fg="white", width=20)
btn_limpiar.pack()

# -------------------------------
# Ejecutar app
# -------------------------------
root.mainloop()