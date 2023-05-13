# estrutura
planeta = {
    'name' : 'Tierra',
    'satelite' : 1
}

# lectura dos alternativas
#1
print(planeta.get('name'))
#2
print(planeta['name']) #mas usado

# modificacion
#1 - update
planeta.update({'name':'jupiter'})
print(planeta['name'])
#2 - asignacion
planeta['name'] = 'tierra'
print(planeta['name'])

# agregar - asignacion
planeta['periodo orbital'] = 360
print(planeta)

# eliminar - pop
print(planeta.pop('periodo orbital')) # devuelve el elemento eliminado
print(planeta)

# datos mas complejos - anidacion
planeta['diametro (km)'] = {
    'polar': 1234,
    'ecuatorial': 12344
}
print(planeta)

# tratamiento de los diccionarios dinamicamente, uso como listas
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

# uso de keys para obtener un objeto de lista de las claves. -> dict_keys(['october', 'november', 'december'])
print(rainfall.keys())
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')

# determinar la existencia de una clave con in
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
print(rainfall['december'])

# uso de values - suma de las precipitaciones
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter')

# Output:
# There was 10.8cm in the last quarter


