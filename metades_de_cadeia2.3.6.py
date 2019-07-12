def main():
    entrada = input('digite uma frase: ')
    tamanho = len(entrada)
    if tamanho % 2 == 0:
        print(entrada[tamanho // 2 - 1: tamanho // 2 + 1])
    else:
        print(entrada[tamanho // 2])


if __name__ == '__main__':
    main()
