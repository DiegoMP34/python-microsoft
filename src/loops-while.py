# Para conocer la sintaxis, un ejericicio
## El usuario quiere ingresar una lista de planetas y mostralos
nuevo_planeta = ""
planetas = []

# realiza la misma intruccion hasta que se cumpla la condicion.
while nuevo_planeta.lower() != "done":
    #verifica si esta vacio
    if nuevo_planeta:
        #agregalo a la lista
        planetas.append(nuevo_planeta)
    #muestra el mensaje
    nuevo_planeta = input("Ingresa un planeta o 'done' cuando termine: ")

#mostramos los planetas ingresados
print(planetas)