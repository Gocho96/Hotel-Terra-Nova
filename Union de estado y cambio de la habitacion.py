#Union del codigo habitacion de hotel y el codigo cambiar estado de la habitacion

habitaciones = [
    {
        "nombre": "Habitación Estándar",
        "tamaño": "20 m²",
        "vista": "Vista al jardín",
        "comodidades": ["Wi-Fi gratis", "Aire acondicionado", "Televisión por cable", "Caja fuerte"],
        "precio": "$50 por noche",
        "reservada": False  # Estado de la habitación
    },
    {
        "nombre": "Habitación Deluxe",
        "tamaño": "35 m²",
        "vista": "Vista al mar",
        "comodidades": ["Wi-Fi gratis", "Aire acondicionado", "Balcón privado", "Minibar", "Caja fuerte", "Televisión por cable"],
        "precio": "$100 por noche",
        "reservada": False  # Estado de la habitación
    },
    {
        "nombre": "Suite Presidencial",
        "tamaño": "50 m²",
        "vista": "Vista panorámica",
        "comodidades": ["Wi-Fi gratis", "Aire acondicionado", "Jacuzzi", "Sala de estar", "Televisión inteligente", "Minibar", "Caja fuerte"],
        "precio": "$300 por noche",
        "reservada": False  # Estado de la habitación
    }
]

def mostrar_detalles(habitacion):
    print("="*40)
    print("Nombre: " + habitacion['nombre'])
    print("Tamaño: " + habitacion['tamaño'])
    print("Vista: " + habitacion['vista'])
    print("Comodidades: " + ", ".join(habitacion['comodidades']))
    print("Precio: " + habitacion['precio'])
    estado = "Reservada" if habitacion['reservada'] else "Disponible"
    print("Estado: " + estado)
    print("Imágenes: [Aquí irían imágenes de ejemplo]")
    print("="*40)

def ver_habitaciones_reservadas():
    print("Habitaciones reservadas:")
    hay_reservadas = False
    for habitacion in habitaciones:
        if habitacion['reservada']:
            print("- " + habitacion['nombre'] + " (Reservada)")
            hay_reservadas = True
    
    if not hay_reservadas:
        print("No hay habitaciones reservadas en este momento.")

def menu():
    while True:
        print("Bienvenido al sistema de reservas del hotel.")
        print("Seleccione una opción:")
        print("1. Ver detalles de una habitación")
        print("2. Ver habitaciones reservadas")
        print("3. Salir")
        
        eleccion = input("Elige una opción: ")
        
        if eleccion == "1":
            print("Seleccione una habitación para ver los detalles:")
            for x in range(len(habitaciones)):
                print(str(x + 1) + ". " + habitaciones[x]['nombre'])
            
            num_habitacion = input("Elige una habitación: ")
            
            if num_habitacion.isdigit():
                num_habitacion = int(num_habitacion) - 1
                
                if 0 <= num_habitacion < len(habitaciones):
                    mostrar_detalles(habitaciones[num_habitacion])
                    
                    print("¿Qué quieres hacer a continuación?")
                    print("1. Volver al menú de búsqueda")
                    print("2. Realizar una reserva")
                    
                    siguiente_accion = input("Elige una opción: ")
                    
                    if siguiente_accion == "1":
                        continue
                    elif siguiente_accion == "2":
                        if not habitaciones[num_habitacion]['reservada']:
                            habitaciones[num_habitacion]['reservada'] = True
                            print("Reserva realizada con éxito. Estado actualizado a 'Reservada'.")
                        else:
                            print("Esta habitación ya ha sido reservada.")
                        continue
                    else:
                        print("Opción no válida. Volviendo al menú principal.")
                else:
                    print("Opción no válida, por favor elige nuevamente.")
            else:
                print("Entrada no válida, por favor introduce un número.")
        
        elif eleccion == "2":
            ver_habitaciones_reservadas()
        
        elif eleccion == "3":
            print("Gracias por usar el sistema de reservas.")
            break
        
        else:
            print("Opción no válida, por favor elige nuevamente.")

# Ejecutar el menú
menu()