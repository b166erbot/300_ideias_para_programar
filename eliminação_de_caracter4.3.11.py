def main():
    entrada = input('digite uma frase: ')
    caracter = input('digite um caracter: ')
    while entrada:
        print(entrada.replace(caracter, ''))
        entrada = input('didite uma frase: ')
        caracter = input('digite um caracter: ')


if __name__ == '__main__':
    main()
