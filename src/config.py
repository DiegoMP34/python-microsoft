# 3. Que pasa si tenemos otro tipo de error
#def main():
#    try:
#        configuration = open('config.txt')
#    except FileNotFoundError:
#        print("Couldn't find the config.txt file!")


#if __name__ == '__main__':
#    main()

#OUTPUT: IsADirectoryError: [Errno 21] Is a directory: 'config.txt'

#Para manejar todo tipo de errores usamos exception
# def main():
#     try:
#         configuration = open('config.txt')
#     except Exception:
#         print("Couldn't find the config.txt file!")

# if __name__ == '__main__':
#     main()

#manejandolo error por error
# def main():
#     try:
#         configuration = open('config.txt')
#     except FileNotFoundError:
#         print("Couldn't find the config.txt file!")
#     except IsADirectoryError:
#         print("Found config.txt but it is a directory, couldn't read it")

# if __name__ == '__main__':
#     main()

#uso de as, para tener al error com variable
try:
    open("mars.jpg")
except FileNotFoundError as err:
    print("got a problem trying to read the file:", err)

#Para excepciones mas genericas, se puede ingresar al err
## por ejemplo OSError que abarca tanto FileNotFoundError 
try:
    open('mars.jpg')
except OSError as err :
    if(err.errno == 2):
        print("Couldn't find the config.txt file!")
    elif err.errno == 13:
        print("Found config.txt but couldn't read it")