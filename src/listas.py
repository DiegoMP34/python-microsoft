# estrutura de una lista
planetas = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Urano", "Neptune"]

# acceder a los valores - el indicador empieza en 0
print(planetas[0], planetas[1])

# reasignacion
planetas[3] = "Planeta rojo"
print(planetas[3]) 

# longitud de la lista o numero de elementos
print(len(planetas))

# agregar valores al final 
planetas.append("Pluto")
print(planetas)

#eleminar valores desde el final
planetas.pop()
print(planetas)

# indices negativos
print(planetas[-1]) # el final de la lista
print(planetas[-2]) # el PENULTIMO de la lista

# encontrar el indice o buscar un valor 
jupiter_indice = planetas.index("Jupiter")
print(f"El planeta numero {jupiter_indice+1} es jupiter")

# uso de numero en listas
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

# uso de min y max
print(min(gravity_on_planets), max(gravity_on_planets))
