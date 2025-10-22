import tkinter as tk
from tkinter import ttk, messagebox

# -------------------------------
# Variables globales (a usar)
# -------------------------------

# Aquí puedes guardar la lista de estudiantes registrados
registros = []

# -------------------------------
# Funciones (a completar por los alumnos)
# -------------------------------

def registrar_estudiante():

    alumno = entry_nombre.get().strip()
    if not alumno:
        messagebox.showwarning("Advertencia", "Por favor ingrese un nombre.")
        return
    
    edad = entry_edad.get().strip()
    if not edad.isdigit() or not (1 <= int(edad) <= 120):
        messagebox.showwarning("Advertencia", "Por favor ingrese una edad válida.")
        return
    
    carrera = combo_carrera.get()
    if not carrera:
        messagebox.showwarning("Advertencia", "Por favor seleccione una carrera.")
        return
    modalidadSeleccionada = modalidad.get()
    if modalidadSeleccionada == "":
        messagebox.showwarning("Advertencia", "Debe seleccionar una modalidad.")
        return
    cursosOpcionales = []
    if curso_python.get():
        cursosOpcionales.append("Python")
    if curso_ia.get():
        cursosOpcionales.append("Inteligencia Artificial")
    if curso_datos.get():
        cursosOpcionales.append("Ciencia de Datos")
    
    registros.append({
        "nombre": alumno,
        "edad": edad,
        "carrera": carrera,
        "modalidad": modalidadSeleccionada,
        "cursos": cursosOpcionales
    })
    
    listbox_registros.insert(tk.END, f"{alumno:<15} | {edad:<3} años | {carrera:<15} | {modalidadSeleccionada:<10} | {', '.join(cursosOpcionales) if cursosOpcionales else 'Ninguno'}")

    
    """
    1. Leer los valores de los campos de entrada.
    2. Validar que nombre y edad no estén vacíos.
    3. Obtener la modalidad seleccionada (Radiobutton).
    4. Obtener los cursos marcados (Checkbuttons).
    5. Agregar el registro a la lista 'registros'.
    6. Mostrar el resumen en el Listbox.
    """
    # TODO: Implementar la lógica de registro
    pass


def limpiar_formulario():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    modalidad.set("")
    combo_carrera.set("")
    curso_python.set(False)
    curso_ia.set(False)
    curso_datos.set(False)
    """
    Restablecer todos los campos del formulario:
    - Vaciar Entry de nombre y edad.
    - Deseleccionar modalidad.
    - Desmarcar cursos.
    """
    # TODO: Implementar limpieza de campos
    pass

def eliminar_registro():
    listbox_registros.delete(tk.ANCHOR)
    if not listbox_registros.curselection():
        messagebox.showwarning("Advertencia", "Por favor seleccione un registro para eliminar.")
        return

    """
    Eliminar el estudiante seleccionado del Listbox y de la lista 'registros'.
    Validar que haya algo seleccionado.
    """
    # TODO: Implementar eliminación
    pass


def mostrar_resumen():
    nombre_list = [alumno["nombre"] for alumno in registros]
    edad_list = [alumno["edad"] for alumno in registros]
    modalidad_list = [alumno["modalidad"] for alumno in registros]
    curso_python_count = sum(1 for alumno in registros if "Python" in alumno["cursos"])
    curso_ia_count = sum(1 for alumno in registros if "Inteligencia Artificial" in alumno["cursos"])
    curso_datos_count = sum(1 for alumno in registros if "Ciencia de Datos" in alumno["cursos"])
    resumen_texto = "\n=== RESUMEN DE ESTUDIANTES REGISTRADOS ===\n" + f"Total de estudiantes: {len(registros)}" + f"\nModalidad Presencial: {modalidad_list.count('Presencial')}" + f"\nModalidad Virtual: {modalidad_list.count('Virtual')}" + f"\nCurso Python: {curso_python_count}" + f"\nCurso Inteligencia Artificial: {curso_ia_count}" + f"\nCurso Ciencia de Datos: {curso_datos_count}"
    messagebox.showinfo("Resumen de Estudiantes", resumen_texto)

    """
    Mostrar con messagebox.showinfo un resumen:
    - Total de estudiantes registrados
    - Cuántos son modalidad Presencial y cuántos Virtual
    - Cuántos eligieron el curso de Python, IA, etc.
    """
    # TODO: Calcular totales y mostrar resumen
    pass


# -------------------------------
# Ventana principal
# -------------------------------
root = tk.Tk()
root.title("Registro de Estudiantes")
root.geometry("650x500")
root.resizable(False, False)
root.config(bg="#f0f0f0")

# -------------------------------
# Frame principal
# -------------------------------
frame = tk.Frame(root, padx=15, pady=15, bg="#ffffff", relief="groove", bd=2)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# -------------------------------
# Sección de datos personales
# -------------------------------
tk.Label(frame, text="Datos del estudiante", font=("Arial", 12, "bold"), bg="#ffffff").grid(row=0, column=0, columnspan=2, sticky="w")

tk.Label(frame, text="Nombre:", bg="#ffffff").grid(row=1, column=0, sticky="w", pady=3)
entry_nombre = tk.Entry(frame, width=25)
entry_nombre.grid(row=1, column=1, sticky="w")
entry_nombre.focus()

tk.Label(frame, text="Edad:", bg="#ffffff").grid(row=2, column=0, sticky="w", pady=3)
entry_edad = tk.Entry(frame, width=10)
entry_edad.grid(row=2, column=1, sticky="w")

tk.Label(frame, text="Carrera:", bg="#ffffff").grid(row=3, column=0, sticky="w", pady=3)
combo_carrera = ttk.Combobox(frame, values=["Ingeniería", "Administración", "Diseño", "Psicología"], state="readonly", width=22)
combo_carrera.grid(row=3, column=1, sticky="w")

# -------------------------------
# Modalidad (Radiobutton)
# -------------------------------
tk.Label(frame, text="Modalidad:", bg="#ffffff").grid(row=4, column=0, sticky="w", pady=5)
modalidad = tk.StringVar(value="")

tk.Radiobutton(frame, text="Presencial", variable=modalidad, value="Presencial", bg="#ffffff").grid(row=4, column=1, sticky="w")
tk.Radiobutton(frame, text="Virtual", variable=modalidad, value="Virtual", bg="#ffffff").grid(row=5, column=1, sticky="w")

# -------------------------------
# Cursos opcionales (Checkbutton)
# -------------------------------
tk.Label(frame, text="Cursos adicionales:", bg="#ffffff").grid(row=6, column=0, sticky="nw", pady=5)
curso_python = tk.BooleanVar()
curso_ia = tk.BooleanVar()
curso_datos = tk.BooleanVar()

tk.Checkbutton(frame, text="Python", variable=curso_python, bg="#ffffff").grid(row=6, column=1, sticky="w")
tk.Checkbutton(frame, text="Inteligencia Artificial", variable=curso_ia, bg="#ffffff").grid(row=7, column=1, sticky="w")
tk.Checkbutton(frame, text="Ciencia de Datos", variable=curso_datos, bg="#ffffff").grid(row=8, column=1, sticky="w")

# -------------------------------
# Botones de acción
# -------------------------------
frame_botones = tk.Frame(frame, bg="#ffffff")
frame_botones.grid(row=9, column=0, columnspan=2, pady=10)

btn_registrar = tk.Button(frame_botones, text="Registrar", command=registrar_estudiante, bg="#4CAF50", fg="white", width=15)
btn_registrar.grid(row=0, column=0, padx=5)

btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_formulario, bg="#f39c12", fg="white", width=15)
btn_limpiar.grid(row=0, column=1, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar", command=eliminar_registro, bg="#e74c3c", fg="white", width=15)
btn_eliminar.grid(row=0, column=2, padx=5)

btn_resumen = tk.Button(frame_botones, text="Resumen", command=mostrar_resumen, bg="#2980b9", fg="white", width=15)
btn_resumen.grid(row=0, column=3, padx=5)

# -------------------------------
# Lista de estudiantes registrados
# -------------------------------
tk.Label(frame, text="Estudiantes registrados:", bg="#ffffff", font=("Arial", 11, "bold")).grid(row=10, column=0, columnspan=2, sticky="w", pady=(10, 5))
listbox_registros = tk.Listbox(frame, width=60, height=8)
listbox_registros.grid(row=11, column=0, columnspan=2, pady=5)
listbox_registros.insert(tk.END, )

# -------------------------------
# Ejecutar aplicación
# -------------------------------
root.mainloop()