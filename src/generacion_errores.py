#Los astronautas limitan su uso de agua a unos 11 litros al día. 
#Vamos a crear una función que, en base al número de astronautas, 
#pueda calcular la cantidad de agua quedará después de un día o más
def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    return f"Total water left after {days_left} days is: {total_water_left} liters"


print(water_left(5,100,2))