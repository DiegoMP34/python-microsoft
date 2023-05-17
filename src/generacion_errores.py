#Los astronautas limitan su uso de agua a unos 11 litros al día. 
#Vamos a crear una función que, en base al número de astronautas, 
#pueda calcular la cantidad de agua quedará después de un día o más
def water_left(astronauts, water_left, days_left):
    #usado para manejar los errores de tipo de datos colocados en los argumentos
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypeError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    #generamos una excepcion para alertar
    if total_water_left < 0:
        raise RuntimeError(f"No hay suficiente agua para {astronauts} astronautas despues de {days_left} dias!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

print(water_left("e",1,"12"))
print(water_left(5,100,2))