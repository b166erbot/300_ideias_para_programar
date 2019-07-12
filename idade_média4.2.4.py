def main():
    idades = []
    idade = int(input('digite uma idade: '))
    if idade <= 0:
        exit()
    while idade > 0:
        idades.append(idade)
        idade = int(input('digite uma idade: '))
    print(sum(idades) / len(idades))


if __name__ == '__main__':
    main()
