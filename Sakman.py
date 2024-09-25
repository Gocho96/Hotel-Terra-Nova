"""
Debe imprimirse un listado de todas las habitaciones que el administrador a registrado en el sistema.

Debe instarse al usuario a escoger una de las habitaciones del listado.

"""


 habitaciones = {
    'Matrimonial': 5,
    'Duo': 10,
    'Solitario': 8
}



def m_habitaciones(habitaciones):
	print("Las Habitaciones Disponibles en Hotel Terra Nova Son: ")

	for tipo, cantidad in habitaciones.items():
		print(f"{tipo} : {cantidad} habitaciones Disponibles")



def e_habitacion(habitaciones):
	print("Las habitaciones a elegir son: ")
	tipo_de_habitacion = list(habitaciones.keys())

	for i, tipo in enumerate(tipo_de_habitacion, 1):
		print(f"{i}. {tipo}")


	n = int(input("Que habitacion vas a elegir? ")) -1


	if n in range(len(tipo_de_habitacion)):
		print("Usted ha elegido la habitacion: ", {tipo_de_habitacion[n]})
	else:
		print("Seleccion invalida, Por favor elija correctamente.")




m_habitaciones(habitaciones)
e_habitacion(habitaciones)
