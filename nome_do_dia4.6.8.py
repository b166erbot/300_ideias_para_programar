def main():
    t = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
    semana = dict(enumerate(t, 1))
    dia = int(input('digite um número de 1-7: '))
    if dia not in range(1, 8):
        raise ValueError('número não está no intervalo de 1-7')
    print(semana[dia])


if __name__ == '__main__':
    main()
