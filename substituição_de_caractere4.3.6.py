def main():
    entrada = input('digite uma frase: ')
    while entrada:
        caracter = input('digite um caracter: ')
        print(entrada.replace(' ', caracter))


if __name__ == '__main__':
    main()
