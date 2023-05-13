# for - estrutura, con un ejercicio
## hacer la cuenta atras de un despegue, se usa sleep, 
## para tener un segundo de espera entre cada elemento que recorre.
from time import sleep

countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second

print("Despegueeee!! 🚀")