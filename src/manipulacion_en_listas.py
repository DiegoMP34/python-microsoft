# segmentacion - sintaxis
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth) #-> Output: ['Mercury', 'Venus']

planetas_despues_tierra = planets[3:]
print(planetas_despues_tierra)

#combinacion
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print(f"The regular satellite moons of Jupiter are {regular_satellite_moons}")

# Output
# The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa', 'Ganymede', 'Callisto']

#ordenacion
planets.sort()
print(planets)
planets.sort(reverse=True)
print(planets)

numeros = [2,1,10,9,4]
numeros.sort()
print(numeros)