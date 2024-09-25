"""
Como huésped, quiero ver detalles completos de la habitación seleccionada, 
incluidas imágenes, para tomar una decisión informada sobre mi reserva.

Criterios de Aceptación:

La página de detalles de la habitación debe mostrar una galería de imágenes, 
descripción detallada de las comodidades, tamaño de la habitación, vista, etc.
Debe haber un botón para regresar al menú de búsqueda o realizar una reserva.
"""

habitaciones = [
    {
        "nombre": "Habitación Estándar",
        "tamaño": "20 m²",
        "vista": "Vista al jardín",
        "comodidades": ["Wi-Fi gratis", "Aire acondicionado", "Televisión por cable", "Caja fuerte"],
        "precio": "$50 por noche"
    },
    {
        "nombre": "Habitación Deluxe",
        "tamaño": "35 m²",
        "vista": "Vista al mar",
        "comodidades": ["Wi-Fi gratis", "Aire acondicionado", "Balcón privado", "Minibar", "Caja fuerte", "Televisión por cable"],
        "precio": "$100 por noche"
    },
    {
        "nombre": "Suite Presidencial",
        "tamaño": "50 m²",
        "vista": "Vista panorámica",
        "comodidades": ["Wi-Fi gratis", "Aire acondicionado", "Jacuzzi", "Sala de estar", "Televisión inteligente", "Minibar", "Caja fuerte"],
        "precio": "$300 por noche"
    }
]

def mostrar_detalles(habitacion):
    print("="*40)
    print("Nombre: " + habitacion['nombre'])
    print("Tamaño: " + habitacion['tamaño'])
    print("Vista: " + habitacion['vista'])
    print("Comodidades: " + ", ".join(habitacion['comodidades']))
    print("Precio: " + habitacion['precio'])
    print("Imágenes: [Aquí irían imágenes de ejemplo]")
    print("="*40)

def menu():
    while True:
        print("Bienvenido al sistema de reservas del hotel.")
        print("Seleccione una habitación para ver los detalles:")
        
        for x in range(len(habitaciones)):
            print(str(x + 1) + ". " + habitaciones[x]['nombre'])
        
        print(str(len(habitaciones) + 1) + ". Salir")
        
        eleccion = input("Elige una opción: ")
        
        if eleccion.isdigit():
            eleccion = int(eleccion)
            
            if 1 <= eleccion <= len(habitaciones):
                mostrar_detalles(habitaciones[eleccion - 1])
                
                print("¿Qué quieres hacer a continuación?")
                print("1. Volver al menú de búsqueda")
                print("2. Realizar una reserva")
                
                siguiente_accion = input("Elige una opción: ")
                
                if siguiente_accion == "1":
                    continue
                elif siguiente_accion == "2":
                    print("Reserva realizada con éxito.")
                    break
                else:
                    print("Opción no válida. Volviendo al menú principal.")
            elif eleccion == len(habitaciones) + 1:
                print("Gracias por usar el sistema de reservas.")
                break
            else:
                print("Opción no válida, por favor elige nuevamente.")
        else:
            print("Entrada no válida, por favor introduce un número.")

# Ejecutar el menú
menu()