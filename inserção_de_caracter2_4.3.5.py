def main():
    caracter = input('digite um caracter: ')
    entrada = input('digite uma palavra: ')
    while entrada:
        print(caracter.join(entrada))
        entrada = input('digite uma palavra: ')


if __name__ == '__main__':
    main()
