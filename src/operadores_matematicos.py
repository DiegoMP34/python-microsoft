suma = 30 + 12 #-> 42
resta = 30 - 12 #-> 18
producto = 30 * 12 #-> 360
cociente = 30 / 12 #-> 2.5

# uso de division - division de multiplo inferior
## convierte 1042 seg a minutos y segundos
minutos = 1042 / 60 ## 60 segundos
print(minutos) #-> 17.366666666666667

## solo queremos 17, usamos // (llamado division de multiplo inferior)
display_minutos = 1042 // 60
print(display_minutos)

## y para los segundos podemos usar modulo (%), para saber el resto de la division
display_segundos = 1042 % 60
print(display_segundos)

#orden de las operaciones
result1 = 40 + 22 * 2
result2 = (40 + 22) * 2 ## se respeta mas el parentesis
result3 = 40 + 22 * 2
print(result1,result2, result3)