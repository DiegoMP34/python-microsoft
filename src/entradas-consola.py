#como trabajar con argumentos desde consola.
import sys

print(sys.argv) ## ['entradas-consola.py', '2023-05-6']
print(sys.argv[0]) ## entradas-consola.py
print(sys.argv[1]) ## 2023-05-6

# en consola al momento de ejecutar el programa le pasamos un argumento
# de esta manera -> python3 entradas-consola.py 2023-05-6

#capturar datos del usuario
print('Bienvenido al este humilde programa')
userName = input('Ingresa tu nombre: ')
print("Saludos " + userName)

#trabajo con numeros
print("Ingresa los numeros que quiera sumar")
number1 = input('Ingresa numero 1: ')
number2 = input('Ingresa numero 2: ')
print(int(number1) + int(number2))