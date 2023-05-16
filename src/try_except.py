#Manejo de errores
## 1. Seguimiento - leer el seguimiento de las excepciones que se generan

## 2. Prueba y excepcion - evita el seguimiento
try:
    open('config.txt')
except FileNotFoundError:
    print("No se encontro el archivo config.txt")
## este tipo de manejo, solo aplica para los errores FileNotFoundError




