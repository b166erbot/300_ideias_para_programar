def main():
    print('escolha uma opção: codificar/decodificar (1/2)')
    opção = int(input('opção: '))
    entrada = input('digite uma frase com caracteres de 32 à 122: ')
    while any([ord(a) not in range(32, 123) for a in entrada]):
        print('entrada inválida.')
        entrada = input('digite uma frase com caracteres de 32 à 122: ')
    if opção == 1:
        cifra = [chr(ord(a) + 1) if ord(a) != 122 else chr(32) for a in entrada]
        print(''.join(cifra))
    else:
        cifra = [chr(ord(a) - 1) if ord(a) != 32 else chr(122) for a in entrada]
        print(''.join(cifra))


if __name__ == '__main__':
    main()
