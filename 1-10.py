tickets_vendidos = []
contador = 1
categorias = {'Niños': 0, 'Adolescentes': 0, 'Adultos': 0, 'Adultos Mayores': 0}

def calcular_precio(edad):
    if edad < 12:
        categorias['Niños'] += 1
        return 10
    elif 12 <= edad <= 17:
        categorias['Adolescentes'] += 1
        return 15
    elif 18 <= edad <= 59:
        categorias['Adultos'] += 1
        return 25
    else:
        categorias['Adultos Mayores'] += 1
        return 12

def comprar_tickets():
    global contador
    global precio
    while True:

        nombre = input("\nIngrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        precio = calcular_precio(edad)
        codigo = str(contador).zfill(4)
        contador += 1
        ticket = (codigo, nombre, edad, precio)
        tickets_vendidos.append(ticket)
        print(f"Ticket comprado: {codigo} | {nombre}, {edad} años, {precio} soles")

        desea_continuar = input("\n¿Desea comprar otro ticket? (s/n): ").lower()
        if desea_continuar != 's':
            break

def mostrar_tickets_vendidos(tickets_vendidos):
    if len(tickets_vendidos) <= 0:
        print("No tienes tickets comprados.")
    else:
        print(f"\n{'Código':<8} | {'Nombre':<20} | {'Edad':<5} | {'Precio':<6}")
        print("-"*50)
        for x in tickets_vendidos:
            print(f"{x[0]:<8} | {x[1]:<20} | {x[2]:<5} | {x[3]:<6}")

def cancelar_ticket(tickets_vendidos):
    if len(tickets_vendidos) <= 0:
        print("No tienes tickets comprados.")
    else:
        codigoCancelar = input("\nIngrese el código del ticket a cancelar: ")
        encontrado = None

        for x in tickets_vendidos:
            if x[0] == codigoCancelar:
                encontrado = x
                tickets_vendidos.remove(encontrado)
                break
        print(f"Se eliminó el ticket {codigoCancelar} correctamente.")

def ver_estadisticas():
    if len(tickets_vendidos) <= 0:
        print("No tienes tickets comprados, por lo tanto no existen estadisticas.")
    else:
        dicEstadisticas = {'Niños': 0, 'Adolescentes': 0, 'Adultos': 0, 'Adultos Mayores': 0}
        ingresoTotales = 0

        for x in tickets_vendidos:
            edad = x[2]
            precio = x[3]
            ingresoTotales += precio

            if edad < 12:
                dicEstadisticas['Niños'] += 1
            elif 12 <= edad <= 17:
                dicEstadisticas['Adolescentes'] += 1
            elif 18 <= edad <= 59:
                dicEstadisticas['Adultos'] += 1
            else:
                dicEstadisticas['Adultos Mayores'] += 1

        print("\n===== ESTADÍSTICAS DE VENTAS =====")
        for clave, valor in dicEstadisticas.items():
            print(f"{clave}: {valor} ticket(s)")
        print(f"Ingresos totales: {ingresoTotales} soles")

def buscar_ticket():
    if len(tickets_vendidos) <= 0:
        print("No tienes tickets, por lo tanto no hay nada que buscar.")

    else:
        nombreBuscar = input("Ingrese el nombre a buscar: ").lower()
        for x in tickets_vendidos:
            if x[1].lower() == nombreBuscar:
                list=[tuple(x)]
                mostrar_tickets_vendidos(list)
                
def menu():
    while True:
        print("\n=== SISTEMA DE TICKETS ===")
        print("1. Comprar tickets")
        print("2. Ver tickets comprados")
        print("3. Cancelar ticket")
        print("4. Ver estadísticas")
        print("5. Buscar ticket por nombre")
        print("6. Salir")
        print("==========================")

        opcion = int(input("\nSeleccione una opción: "))
        if opcion == 1:
            comprar_tickets()
        elif opcion == 2:
            mostrar_tickets_vendidos(tickets_vendidos)
        elif opcion == 3:
            cancelar_ticket(tickets_vendidos)
        elif opcion == 4:
            ver_estadisticas()
        elif opcion == 5:
            buscar_ticket()
        elif opcion == 6:
            print("Gracias por usar el sistema de tickets. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
menu()