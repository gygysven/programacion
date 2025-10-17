# import tkinter as tk

# ventana = tk.Tk()
# ventana.title("Login")
# ventana.geometry("300x200")
# ventana.resizable(False, False)

# contenedor = tk.Frame(ventana, padx=20, pady=20, bg = "beige")
# contenedor.pack(expand=True, fill='both')

# # USUARIO
# lbl_titulo = tk.Label(
#     contenedor, 
#     text="Usuario", 
#     font=("Arial", 16), 
#     fg = "Brown", bg = "beige",
#     )
# lbl_titulo.pack(pady=(0, 10))
# entrada_usuario = tk.Entry(contenedor, font=("Arial", 14), width=25)
# entrada_usuario.pack(pady=5, padx=5)

# # CONTRASEÑA
# lbl_contraseña = tk.Label(
#     contenedor,
#     text="Contraseña",
#     font=("Arial", 16),
#     fg = "Brown", bg = "beige",
#     )
# lbl_contraseña.pack(pady=(10, 10))
# entrada_contraseña = tk.Entry(contenedor, font=("Arial", 14), width=25, show="*")
# entrada_contraseña.pack(pady=5, padx=5)

# ventana.mainloop()






# Login  nombre para user entry contraseña si es valido vienvenido nombre, invalidos contraseña incorrecta


import tkinter as tk

ventana =tk.Tk()
ventana.title("Login")
ventana.geometry("360x200")

contenedor = tk.Frame(ventana, padx=16, pady=16)
contenedor.pack(fill="both", expand=True)

tk.Label(contenedor,text="Usuario").grid(row=0, column=0, sticky="e", padx=5, pady=5)

entrada_usuario = tk.Entry(contenedor, width=25)
entrada_usuario.grid(row=0, column=1, sticky="w" ,  padx=5, pady=5)

entrada_usuario.focus()

tk.Label(contenedor,text="Contraseña").grid(row=1, column=0, sticky="e", padx=5, pady=5)

entrada_contraseña = tk.Entry(contenedor, width=25)
entrada_contraseña.grid(row=1, column=1, sticky="w" ,  padx=5, pady=5)

entrada_contraseña.focus()

def fn_sesion():
    usuario = entrada_usuario.get().strip()
    if not usuario:
        lbl_mensaje.config(text="Por favor ingrese su usuario. ")

    contraseña = entrada_contraseña.get().strip()
    if contraseña == "123456":
        lbl_mensaje.config(text=f"¡¡Bienvenid@ {usuario}!!")
    else:
        lbl_mensaje_x.config(text="Contraseña incorrecta. Por favor intente de nuevo. ")

btn_saludo = tk.Button (contenedor, text="Iniciar sesión", command=fn_sesion)
btn_saludo.grid(row=2, column=0, columnspan=2, pady=10)

lbl_mensaje_x = tk.Label (contenedor, text="", fg="red")
lbl_mensaje_x.grid(row=3, column=0, columnspan=2, pady=10)

lbl_mensaje = tk.Label (contenedor, text="", fg="green")
lbl_mensaje.grid(row=3, column=0, columnspan=2, pady=10)


ventana.mainloop()