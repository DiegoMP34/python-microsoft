# title() - primera letra en mayusculas de cada palabra
print("Temperaturas y hechos a cerca de la luna".title())

# split() - separa segun el argumento en una lista
temperatures = """Daylight: 260 F 
Nighttime: -280 F """
print(temperatures.split())
print(temperatures.split("\n"))

# in - busqueda de cadena, caracter o palabra; devuelve un booleano
res = "luna" in "este texto describira los hechos y retos de viaje espacial"
res1 = "luna" in "en este texto se describira ls hechos y retos de la luna"
print(res, res1)

# find() - conocer la posicion especifica de palabra, caracter.
moon = """Saturno tiene una temperatura de dia de -170 grados celcius $, 
mientras que marte tiene -28 celcius """
print(moon.find("luna")) ## -1
print(moon.find("Saturno")) ## 0

# count() . couenta las repeticiones de una palabra, caracter
print(moon.count("celcius"))
print(moon.count("$"))

# lower() o upper() - minuscula o mayuscula respectivamente
print(moon.upper())
print(moon.lower()) ## un buen uso es para normalizar el texto y realziar busquedas indepedientemente de M y m
print(moon) ## no cambia la variable, cumple con la reglas

# isnumeric() - identifica si la cadena es un tipo de dato, devuelve boolean
for el in temperatures.split():
    if el.isnumeric():
        print(el) ## devuelve el numero dentro de la cadena

## ejemplo simple
print("14".isnumeric()) ## true

# starswith() y endswith() - devuelve boolean si se cumple el argumento al principio o final respectivamente, de la cadena
print("-12".startswith("-")) ## true
print("-12 C".endswith("C")) ## true

# replace() - remplaza un o mas caracteres especificados
print("12 celsius y 13 celsius".replace("celsius","C"))

# join() - un poco distinto al otros metodos de cadena, aqui se necesita como argumento un elemento iteralble
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
print("-".join(moon_facts)) ## la cadena especifica el caracter de union.
print(" ".join(moon_facts))