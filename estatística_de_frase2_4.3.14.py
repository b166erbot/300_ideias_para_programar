from string import ascii_lowercase as string


def main():
    entrada = input('digite uma frase: ')
    print(f"quantidade de caracteres brancos: {entrada.count(' ')}")
    print(f"quantidade de palavras: {len(entrada.split())}")
    contagem = entrada.count('a') + entrada.count('A')
    print(f"quantidade de ocorrências da letra A: {contagem}")
    for caracter in string:
        quantidade = entrada.count(caracter) + entrada.count(caracter.upper())
        print(f"quantidade de {caracter}: {quantidade}")


if __name__ == '__main__':
    main()
