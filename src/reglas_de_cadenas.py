# N°1 - inmutabilidad de las cadenas
fact = 'la luna no tiene atmosfera.'
fact + 'ahi no se puede escuchar ningun sonido'
print (fact)

#N°2 - uso de comillas 
## uso de comillas dobles
moon_radius = "la luna tiene un radio de 1,080 millas"
## uso de comillas simple, cuando hay comillas dobles
moon_face = '"the near side" es la parte de la luna que encara a la tierra'
## uso de apostrofes
moon_surface = "We only see about 60% of Moon's surface"
## uso de de comillas dobles y apostrofes
moon_info = """ "the near side" es la parte de la luna que encara a la tierra. We only see about 60% of Moon's surface"""

#N°3 uso de multilinea
## usando \n
moon_infos = "la luna tiene un radio de 1,080 millas.\n the near side es la parte de la luna que encara a la tierra.\n We only see about 60% of Moons surface"

print(moon_infos)

## usando comillas triple, mejor ya que nos permite usar tanto las otras comillas y el espaciado de linea

moon = """la luna tiene un radio de 1,080 millas. 
"the near side" es la parte de la luna que encara a la tierra. 
We only see about 60% of Moon's surface """

print(moon)