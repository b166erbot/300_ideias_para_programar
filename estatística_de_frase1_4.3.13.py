def main():
    entrada = input('digite uma frase: ')
    print(f"quantidade de caracteres brancos: {entrada.count(' ')}")
    print(f"quantidade de palavras: {len(entrada.split())}")
    contagem = entrada.count('a') + entrada.count('A')
    print(f"quantidade de ocorrências da letra A: {contagem}")


if __name__ == '__main__':
    main()
