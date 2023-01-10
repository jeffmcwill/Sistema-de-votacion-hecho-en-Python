import os
from dosPreguntas import dosPreguntas
from TresPreguntas import TresPreguntas
from CuatroPreguntas import cuatroPreguntas
from CincoPreguntas import cincoPreguntas


def sumaLista(lista):
	suma = 0
	for elem in lista:
		suma += elem
	return suma

def sistemaconOpcionario():

	user = 0

	while True:
		try:
			print("-------------------------------------")
			print("Bienvenido al sistema con opcionario.")
			print("-------------------------------------")
			print("1.Dos Opciones.")
			print("2.Tres Opciones.")
			print("3.Cuatro Opciones.")
			print("4.Cinco Opciones.")
			print("-------------------------------------")
			print("5.Salir.")
			print("-------------------------------------")
			user = int(input("> "))

			if user == 1:
				print("Eligiendo encuesta de dos opciones.")
				dosPreguntas()
				break

			elif user == 2:
				print("Eligiendo encuesta de tres opciones.")
				TresPreguntas()
				break

			elif user == 3:
				print("Eligiendo encuesta de cuatro opciones.")
				cuatroPreguntas()
				break

			elif user == 4:
				print("Eligiendo encuesta de cinco opciones.")
				cincoPreguntas()
				break

			elif user == 5:
				main()
				break

			else:
				print("El sistema no reconoce el comando ingresado...")
				continue

		except:
			print("Intente nuevamente. COMANDO INCORRECTO.")
			continue

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
				sistema()
				break

			elif res == 2:
				print("Ok, cerrando programa.")
				break

			else:
				print("Numero o comando no encontrado.")

		except:
			print("Comando ingresado incorrecto, vuelva a intentar.")
			continue

def sistema():

	listado = []
	cantidad = 0
	respuesta = 0

	print("¿Que pregunta haras?")
	ask = input("> ")

	while True:
		try:
			print("¿Cuantas veces sera repetida la pregunta(en numero.)?")
			cantidad = int(input("> "))

			for i in range(cantidad):
				os.system("cls")
				print(ask)
				respuesta = input("> ")
				listado.append(respuesta)
				print("Respuesta agregada {}".format(i))

			os.system("cls")
				
			print("----------------")
			print("// CONCLUSION //")
			print("-----------------")
			print("Preguntas:")
			print(ask)
			print("-----------------")
			print("Respuestas: ")
			print(listado)
			print("-----------------")
			print("cantidad de preg:")
			print(cantidad)
			print("-----------------")
			
			continuar()
			break

		except:
			print("Agregue los comandos correctos...")
			continue

def main():

	num2 = 0

	while True:
		
		try:

			print("--------------------------------")
			print("| Sistema Sencillo de votacion |")
			print("|        <(^v^)x(^v^)>         |")
			print("--------------------------------")
			print("1. Hacer votacion.")
			print("2. Sistema con opcionario.")
			print("3. Salir")
			print("---------------------------------")

			num2 = int(input("> "))

			if num2 == 1:
				print("Ok, inicienmos.")
				sistema()
				break

			elif num2 == 2:
				print("Ok, vayamos al opcionario")
				sistemaconOpcionario()
				break

			elif num2 == 3:
				print("Ok, Hasta luego.")
				break

			else:
				print("Numero no encontrado.")
				continue

		except:
			print("Error de sintaxis, agregue la soportada por el programa.")
			continue

#-------------------------------------------------------------------

if __name__ == "__main__":
	main()