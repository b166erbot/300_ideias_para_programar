def main():
    nome_completo = input('digite um nome: ').split()
    while nome_completo:
        print(nome_completo[0])
        nome_completo = input('digite um nome: ').split()


if __name__ == '__main__':
    main()
