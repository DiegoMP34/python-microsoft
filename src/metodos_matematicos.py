# conversion de un string a int o decimal
cadena = "23"
cadena1 = "23.445"
print(int(cadena))
print(float(cadena1))

# valor absoluto, abs
print(abs(40 - 20))
print(20 - 40) 
print(abs(20 - 40)) 

# redondeo - round
print(round(14.6)) #->15
print(round(14.4)) #->14

# uso de bliblioteca math
from math import ceil, floor

redonde_arriba = ceil(13.6)
print(redonde_arriba)

redonde_abajo = floor(13.6)
print(str(redonde_abajo) + "\n\n")

