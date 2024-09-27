habitaciones = {}

def formularioHabitaciones():
    print("---------BIENVENIDO AL HOTEL TERRA NOVA---------")
    print("Sistema de carga de información de habitaciones")
    x = input("¿Ingresarás la información de una habitación? S/N: ")
    contador = 0

    while x == "s" or x == "S":
        tipo = input("Ingrese el tipo de habitación (Matrimonial, Duo, Solitario): ")
        numero = input("Ingrese el número de la habitación: ")
        persona = int(input("Ingrese la cantidad de personas permitidas: "))
        aire = input("¿Incluye aire acondicionado?: ")
        wifi = input("¿Incluye Wi-Fi?: ")
        tv = input("¿Incluye televisión?: ")
        desayuno = input("¿Incluye desayuno?: ")
        precio = float(input("Ingrese el precio de la habitación: "))
        estado = input("Ingrese el estado actual de la habitación (Disponible / No disponible): ")

        habitacion = {
            "tipo": tipo, "numero": numero, "persona": persona, "aire": aire,
            "wifi": wifi, "tv": tv, "desayuno": desayuno, "precio": precio, "estado": estado
        }

        habitaciones[contador] = habitacion
        contador += 1
        x = input("¿Quieres ingresar otra habitación? S/N: ")

def m_habitaciones(habitaciones):
    print("Las Habitaciones Disponibles en Hotel Terra Nova Son: ")
    for key, habitacion in habitaciones.items():
        print(f"{habitacion['tipo']} (Nro: {habitacion['numero']}): {habitacion['estado']}")

def captar_respuesta_habitacion():
    tipo_de_habitacion = list(habitaciones.keys())
    print("Por favor, confirme el tipo de habitación que ha elegido.")
    for i, habitacion in enumerate(habitaciones.values(), 1):
        print(f"{i}. {habitacion['tipo']}")
        
    n = int(input("¿Qué número de habitación vas a elegir? ")) - 1
    if n in range(len(tipo_de_habitacion)):
        return habitaciones[n]
    else:
        print("Selección inválida. Por favor elija correctamente.")
        return None

def mostrar_detalles(habitacion):
    print("="*40)
    print("Tipo: " + habitacion['tipo'])
    print("Número: " + habitacion['numero'])
    print("Capacidad: " + str(habitacion['persona']) + " personas")
    print("Aire acondicionado: " + habitacion['aire'])
    print("Wi-Fi: " + habitacion['wifi'])
    print("Televisión: " + habitacion['tv'])
    print("Desayuno: " + habitacion['desayuno'])
    print("Precio: $" + str(habitacion['precio']) + " por noche")
    print("Estado: " + habitacion['estado'])
    print("="*40)

def reservaHabitacion(habitacion):
    if habitacion['estado'] == "Disponible":
        disponibilidad = input("¿Desea reservar la habitación? (S/N): ")
        if disponibilidad == "S" or disponibilidad == "s":
            habitacion['estado'] = "No disponible"
            print("Habitación reservada exitosamente.")
        else:
            print("No se reservó la habitación.")
    else:
        print("Lo siento, esta habitación ya está reservada.")

def preguntar_volver_a_ver_habitaciones():
    respuesta = input("¿Desea volver a ver las habitaciones? (S/N): ")
    if respuesta == "S" or respuesta == "s":
        return "si"
    elif respuesta == "N" or respuesta == "n":
        return "no"
    else:
        print("Por favor, ingrese 'S' para sí o 'N' para no.")
        return preguntar_volver_a_ver_habitaciones()  # vuelve a preguntar

# Ejecución del código
formularioHabitaciones()

continuar = "si"  # variable para controlar el bucle
print("========================================")

while continuar == "si":
    m_habitaciones(habitaciones)
    habitacion_elegida = captar_respuesta_habitacion()

    if habitacion_elegida is not None:
        mostrar_detalles(habitacion_elegida)
        reservaHabitacion(habitacion_elegida)

    continuar = preguntar_volver_a_ver_habitaciones()  # Actualiza la variable

print("Gracias por usar el sistema de reservas.")
