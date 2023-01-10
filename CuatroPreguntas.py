import os

def sumaLista(lista):
	suma = 0
	for elem in lista:
		suma += elem
	return suma

def continuar():
	
	res = 0

	while res != 1:
		
		try:
			print("-------------------------------------")
			print("Quieres volver a hacer una votacion?")
			print("-------------------------------------")
			print("1. Si")
			print("2. No")
			print("-------------------------------------")
			res = int(input("> "))

			if res == 1:
				print("Ok. vamos al principio.")
				dosPreguntas()
				break

			elif res == 2:
				print("Ok, cerrando programa.")
				break

			else:
				print("Numero o comando no encontrado.")
				continue

		except:
			print("Comando ingresado incorrecto, vuelva a intentar.")
			continue

def cuatroPreguntas():

	listas1 = []
	listas2 = []
	listas3 = []
	listas4 = []
	listado = []

	print("-----------------------------------")
	print("¿Ok, que clase de pregunta haras?: ")
	ask = input("> ")

	while True:
		try:
			print("¿Que dira la primera opcion?")
			opcion1 = input("> ")

			print("¿Que dira la segunda opcion?")
			opcion2 = input("> ")

			print("¿Que dira la tercera opcion?")
			opcion3 = input("> ")

			print("¿Que dira la cuarta opcion?")
			opcion4 = input("> ")

			print("Agregados satisfactoriamente.")
			break
		
		except:
			print("Ingresa comandos correctos...")
			continue

	while True:

		try:
			print("¿Cuantas veces sera repetida la pregunta(en numero.)?")
			cantidad = int(input("> "))

			for i in range(cantidad):
				os.system("cls")
				print(ask)
				print("---------")
				print(opcion1)
				print(opcion2)
				print(opcion3)
				print(opcion4)
				print("---------")
				respuesta = int(input("> "))
				listado.append(respuesta)

				if respuesta == 1:
					contador1 = 1
					listas1.append(contador1)
					print("Respuesta agregada {}".format(i))

				elif respuesta == 2:
					contador2 = 1
					listas2.append(contador2)
					print("Respuesta agregada {}".format(i))

				elif respuesta == 3:
					contador3 = 1
					listas3.append(contador3)
					print("Respuesta agregada {}".format(i))

				elif respuesta == 4:
					contador4 = 1
					listas4.append(contador4)
					print("Respuesta agregada {}".format(i))


			os.system("cls")
				
			print("----------------")
			print("// CONCLUSION //")
			print("-----------------")
			print("Pregunta:")
			print(ask)
			print("-----------------")
			print("Respuestas: ")
			print(listado)
			print("-----------------")
			print("cantidad de preg:")
			print(cantidad)
			print("-----------------")
			print("Cant. elegido 1: ")
			print(sumaLista(listas1))
			print("-----------------")
			print("Cant. elegido 2: ")
			print(sumaLista(listas2))
			print("-----------------")
			print("Cant. elegido 3: ")
			print(sumaLista(listas3))
			print("-----------------")
			print("Cant. elegido 4: ")
			print(sumaLista(listas4))

			if sumaLista(listas1) > sumaLista(listas2) and sumaLista(listas1) > sumaLista(listas3) and sumaLista(listas1) > sumaLista(listas4):
				print("//////////////////////////////////////////////")
				print("La opcion 1 es elegida por la mayoria de voto")
				print("//////////////////////////////////////////////")

			elif sumaLista(listas2) > sumaLista(listas1) and sumaLista(listas2) > sumaLista(listas3) and sumaLista(listas2) > sumaLista(listas4):
				print("//////////////////////////////////////////////")
				print("La opcion 2 es elegida por la mayoria de voto")
				print("//////////////////////////////////////////////")

			elif sumaLista(listas3) > sumaLista(listas1) and sumaLista(listas3) > sumaLista(listas2) and sumaLista(listas3) > sumaLista(listas4):
				print("//////////////////////////////////////////////")
				print("La opcion 3 es elegida por la mayoria de voto")
				print("//////////////////////////////////////////////")

			elif sumaLista(listas4) > sumaLista(listas1) and sumaLista(listas4) > sumaLista(listas2) and sumaLista(listas4) > sumaLista(listas3):
				print("//////////////////////////////////////////////")
				print("La opcion 4 es elegida por la mayoria de voto")
				print("//////////////////////////////////////////////")

			elif sumaLista(listas1) == sumaLista(listas2) and sumaLista(listas1) == sumaLista(listas3) and sumaLista(listas1) == sumaLista(listas4):
				print("////////////////////////////////////////////////")
				print("EMPATE EN LAS OPCIONES... No hay conclusiones :C")
				print("////////////////////////////////////////////////")
			
			continuar()
			break

		except:
			print("Agregue los comandos correctos...")
			continue

if __name__ == "__main__":
	cuatroPreguntas()