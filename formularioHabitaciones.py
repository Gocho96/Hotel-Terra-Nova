def formularioHabitaciones():
    habitaciones={}

    print("---------BIENVENIDO AL HOTEL TERRA NOVA---------")
    print("Sistema de carga de información de habitaciones")
    x=input("¿Ingresarás la información de una habitación? S/N: ")
    contador=0

    while x == "s" or x=="S":
        tipo=input("Ingrese el tipo de habitación (Matrimonial, Duo, Solitario): ")
        numero=input("Ingrese el número de la habitación: ")
        persona=int(input("Ingrese la cantidad de personas permitidas: "))
        aire=input("¿Incluye aire acondicionado?: ")
        wifi=input("¿Incluye Wi-Fi?: ")
        tv=input("¿Incluye televisión?: ")
        desayuno=input("¿Incluye desayuno?: ")
        precio=float(input("Ingrese el precio de la habitación: "))
        estado=input("Ingrese el estado actual de la habitación (Disponible / No disponible): ")

        habitacion = {
            "tipo": tipo, "numero": numero, "persona": persona, "aire": aire, "wifi": wifi, "tv": tv, "desayuno": desayuno, "precio": precio, "estado": estado
        }

        habitaciones[contador]=habitacion

        x = input("¿Quieres ingresar otra habitación? S/N: ")
        if x == "s" or x == "S":
            contador+=1

formularioHabitaciones()
