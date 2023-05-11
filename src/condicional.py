#sintaxis de una sentecia if
a = 23
b = 10

## ojo: se debe tener una sangria des pues de cada sentencia, 
## para que pertenesca al bloque de codigo de la condicion evaluada
if a > b :
    print('a es mayor que b')

#instrucion else if
if b < a :
    print('b es menor que a')
else:
    print('a es mayor que b')

#sentecias elif
p = 5
q = 10

if p >= q:
    print('p es mayor o igual que q')
elif q > p:
    print('q es mayor que p') 

#se puede usar else antes que elif?
if p >= q:
    print('p es mayor o igual que q')
#else:
#    print('usamos else antes de elif')
elif q > p:
    print('q es mayor que p')
#nos muestra que es una sintaxis invalida

#uso de and y or
if p == 10 or q == 10:
    print(p + q)

if p > 1 and q > 9:
    print(q * p)