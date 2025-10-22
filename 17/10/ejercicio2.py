import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Ventana de Bebidas")
ventana.geometry("420x520")
ventana.resizable(False, False)

frame_principal = tk.Frame(ventana, bg="#84ADD8")
frame_principal.pack(padx=10, pady=10, fill="both", expand=True) 
# "Pack" para mostrar

frame_opciones = tk.LabelFrame(
    frame_principal, 
    text="Seleccione sus bebidas", 
    font=("Arial", 14, "bold"),
    fg="#ffffff",
    bg="#5790be"
)
frame_opciones.pack(padx=10, pady=10, fill="x")

refresco_var = tk.BooleanVar()    # Valor por defecto: Falso
jugo_var = tk.BooleanVar()
agua_var = tk.BooleanVar()

# PRECIO DE BEBIDAS
precio_refresco = 10
precio_jugo = 15
precio_agua = 5

# CREACION DE CHECKBUTTONS
check_refresco = tk.Checkbutton(
    frame_opciones,
    text=f"Refresco - S/ {precio_refresco}",
    variable = refresco_var,
    onvalue = True,
    offvalue = False,
    bg = "#809AD3", anchor="w"
    )
check_refresco.pack(fill="x", padx=10, pady=5)

check_jugo = tk.Checkbutton(
    frame_opciones,
    text=f"Jugo - S/ {precio_jugo}",
    variable = jugo_var,
    onvalue = True,
    offvalue = False,
    bg = "#95c1e6", anchor="w"
    )
check_jugo.pack(fill="x", padx=10, pady=5)

check_agua = tk.Checkbutton(
    frame_opciones,
    text=f"Agua - S/ {precio_agua}",
    variable = agua_var,
    onvalue = True,
    offvalue = False,
    bg = "#9FBDE6", anchor="w"
    )
check_agua.pack(fill="x", padx=10, pady=5)

# frame_resumen = tk.LabelFrame(ventana, bg = "lightblue")
# frame_principal.pack(padx=10, pady=10, fill="both", expand=True)

frame_resumen = tk.LabelFrame(
    frame_principal, 
    text="Resumen del pedido", 
    font=("Arial", 14, "bold"),
    fg="#ffffff",
    bg="#5790be"
)
frame_resumen.pack(padx=10, pady=10, fill="x")

label_resumen = tk.Label(
    frame_resumen,
    text = "Tu pedido aparecerá aquí en breve...",
    font = ("Arial", 12, "italic"),
    bg = "#5790be",
    fg= "white"
)

label_resumen.pack(padx=10, pady=10, fill="x")

def calcular_total():
    total = 0
    pedido = []

    if refresco_var.get():
        total += precio_refresco
        pedido.append(f"Refresco - S/ {precio_refresco}")

    if jugo_var.get():
        total += precio_jugo
        pedido.append(f"Jugo - S/ {precio_jugo}")

    if agua_var.get():
        total += precio_agua
        pedido.append(f"Augo - S/ {precio_agua}")

    if not pedido:
        messagebox.showwarning("Error", "Por favor seleccione al menos una bebida.")
        return

    resumen_texto= "Detalle del pedido:\n" + "\n".join(pedido) + f"\n\nTotal a pagar: S/{total}"
    label_resumen.config(text=resumen_texto)

btn_calcular = tk.Button(frame_principal, text="Calcular",
        font=("Arial", 10, "bold"),
        bg = "#35439C", command = calcular_total
)
btn_calcular.pack(padx=10, pady=10)


# btn_saludo = tk.Button (contenedor, text="Iniciar sesión", command=fn_sesion)
# btn_saludo.grid(row=2, column=0, columnspan=2, pady=10)

ventana.mainloop()