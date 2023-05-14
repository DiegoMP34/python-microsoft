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