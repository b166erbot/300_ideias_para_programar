def main():
    semana = dict(enumerate(
        ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta'], 1))
    dia = int(input('digite um dia da semana: '))
    if day not in range(1, 8):
        raise ValueError('dia fora do intervalo semanal.')
    print(semana[dia])


if __name__ == '__main__':
    main()
