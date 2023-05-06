#como trabajar con argumentos desde consola.
import sys

print(sys.argv) ## ['entradas-consola.py', '2023-05-6']
print(sys.argv[0]) ## entradas-consola.py
print(sys.argv[1]) ## 2023-05-6

# en consola al momento de ejecutar el programa le pasamos un argumento
# de esta manera -> python3 entradas-consola.py 2023-05-6

