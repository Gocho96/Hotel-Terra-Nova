habitaciones =[]

def reservaHabitacion (habitaciones):
    disponibilidad = input("Ingrese si quiere reservar la habitacion SI/NO: ").upper().strip()
    if disponibilidad == "SI":
        mensaje = "Habitacion reservada exitosamente"
    else:
        mensaje= "No se reservo la habitacion"

    return mensaje

reservaHabitacion = reservaHabitacion (habitaciones)
print (reservaHabitacion )
