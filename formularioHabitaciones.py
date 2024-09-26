def formularioHabitaciones():
    habitaciones={}
    tipos=[]
    numeros=[]
    personas=[]
    aires=[]
    wifis=[]
    tvs=[]
    desayunos=[]
    precios=[]
    estados=[]

    print("---------BIENVENIDO AL HOTEL TERRA NOVA---------")
    print("Sistema de carga de información de habitaciones")
    x = input("¿Ingresarás la información una habitación? S/N: ")
    contador=0

    while x == "s" or x=="S":
        tipo=input("Ingrese el tipo de habitación (Matrimonial, Duo, Solitario): ")
        tipos.append(tipo)
        numero=input("Ingrese el número de la habitación: ")
        numeros.append(numero)
        persona=int(input("Ingrese la cantidad de personas permitidas: "))
        personas.append(persona)
        aire=input("¿Incluye aire acondicionado?: ")
        aires.append(aire)
        wifi=input("¿Incluye aire Wi-Fi?: ")
        wifis.append(wifi)
        tv=input("¿Incluye televisión?: ")
        tvs.append(tv)
        desayuno=input("¿Incluye desayuno?: ")
        desayunos.append(desayuno)
        precio=float(input("Ingrese el precio de la habitación: "))
        precios.append(precio)
        estado=input("Ingrese el estado actual de la habitación (Disponible / No disponible): ")
        estados.append(estado)
        x = input("¿Quieres ingresar otra habitación? S/N: ")
        if x == "s" or x == "S":
            contador+=1
