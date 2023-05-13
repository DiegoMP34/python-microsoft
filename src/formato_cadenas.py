# formato de texto con %, usamos print para mostrar el formato
porcentaje_masa = "1/6"
print("En la luna, pesarias cerca %s de tu peso en la tierra" % porcentaje_masa)

## uso de varios argumentos, pero no es muy legible
print("""Both sides of the %s get the same amount of sunlight,
but only one side is seen from %s because
the %s rotates around its own axis when it orbits %s.\n""" % ("Moon", "Earth", "Moon", "Earth"))

#uso de format(), con uso el {} que representa a el argumento
print("En la luna, pesarias cerca {} de tu peso en la tierra\n".format(porcentaje_masa))

## se puede usar para diferenciar las variables en los argumentos, numeros entre los {}
print("""You are lighter on the {0}, because on the {0} 
you would weigh about {1} of your weight on Earth\n""".format("Moon", porcentaje_masa))

## pero para hacerlo mas legible seria mejor usar identificadores mas precisos entre los {}
print("""You are lighter on the {moon}, because on the {moon} 
you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=porcentaje_masa))

#uso de f-strings, son como platillas, para su uso se tiene que colocar una f primero, y {}
print(f"En la luna, pesarias cerca {porcentaje_masa} de tu peso en la tierra\n")

## ademas se puede hacer uso de expresiones o llamadas de funciones
print(f"En la luna, pesarias cerca {round(100/6,1)}% de tu peso en la tierra\n")