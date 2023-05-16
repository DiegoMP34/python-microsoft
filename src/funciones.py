# sintaxis de la funciones
def partes_cohete ():
    print("carga explusiva, propulsor, estrutura")

#llamar o ejecutar una funcion
partes_cohete() ## esta es una funcion sin argumentos

# en python, una funcion sin argumentos devuelve none
salida = partes_cohete()
print(salida)
print(salida is None)

# para que devuelva un valor se le tiene que colocar la sentencia return
def partes_cohete1():
    return "carga explusiva, propulsor, estrutura"

output = partes_cohete1()
print(output)

#algunas funciones, pueden o no tener argumentos
## como any(), este necesita un objeto iterable
print(any([False,True,False])) ## any() devuelve un true si existe al menos un true
print(any([False,False,False])) ## o false si no hay true

#exiten funciones como str()
print(str()) # que si no le indicas argumentos, este regresa un string vacio
print(str(13)) # o comvierte el argumento dado a cadena.
## a diferencia de any(), str() sin argumentos no devuelve error como si lo hace any().

# funcion con argumento
def distancia_desde_tierra(destino):
    if destino == "Luna":
        return "238,855"
    else:
        return "No disponible para computar ese destino"

# si llamamos a la funcion sin argumento no devuelve error
print(distancia_desde_tierra("Luna"))
print(distancia_desde_tierra("Marte"))

# funcion con varios argumentos, usamos coma
def dias_a_completar(distancia, velocidad):
    hours =  distancia/velocidad
    return hours/24

#podemos calcular los dias para llegar a la luna
print(dias_a_completar(238855, 75))

#se pueden tener funciones como argumentos 
print(round(dias_a_completar(238855,75))) #esto puede afectar a la legilibilidad

#argumentos de palabra clave - son argumentos asignados a un valor predeterminado
## time delta ayuda en la suma de un tipo date.
from datetime import timedelta, datetime

def tiempo_llegada(hora=51):
    actual = datetime.now()
    llegada = actual + timedelta(hours=hora)
    return llegada.strftime("Llegada: %A %H:%M")

print(tiempo_llegada())
print(tiempo_llegada(0))
print(datetime.now())

# combinacion de argumentos y argumentos de palabra clave
def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

#arrival_time() #error: al menos un argumento
print(arrival_time('Moon')) 
print(arrival_time('Orbit', hours=0.13))

#variable de argumentos - permite pasar cualquier numero de argumentos, incluido 0
## Para definirlo tenemos colocar * y despues
## Se usa generalmente args o a para definir este argumento
def varible_lenght(*args):
    print(args)

varible_lenght()
varible_lenght("one","two")
varible_lenght(None)

def secuencia_tiempo(*args):
    total_minutos = sum(args)
    if total_minutos < 60:
        print(f"Tiempo total de despege {total_minutos} minutos")
    else:
        print(f"Tiempo total de despege {total_minutos/60} horas")

secuencia_tiempo()
secuencia_tiempo(4,14,18)
# la variable se le denomina catch-all

#Combinacion entre palabra clave y variable de argumentos
def miembros_crew(**kwargs):
    print(f"{len(kwargs)} astronautas fueron asignados para esta mision, son:")
    print(kwargs.items())
    for title, name in kwargs.items():
        print(f"{title} : {name}")

miembros_crew(captain = 'Neil Armstrong', pilot = "Buzz aldrin", command_pilot="Michael Collins")