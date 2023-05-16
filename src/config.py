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
def main():
    try:
        configuration = open('config.txt')
    except Exception:
        print("Couldn't find the config.txt file!")

if __name__ == '__main__':
    main()