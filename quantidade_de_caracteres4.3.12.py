def main():
    entrada = input('digite uma frase: ')
    caracter = input('digite um caracter: ')
    print(entrada.count(caracter.lower()) + entrada.count(caracter.upper()))


if __name__ == '__main__':
    main()
