def all_combinations(iterable):
    for item in iterable:
        for item2 in iterable:
            yield f"{item} {item2}"


def main():
    ganhos = (0, 0.25, 0.5, 0.7, 1, 1.25, 1.5, 1.75, 2)
    fichas = dict(zip(all_combinations(('roxo', 'laranja', 'verde')), ganhos))
    valor = float(input('digite o valor da aposta R$: '))
    if valor > 100:
        raise ValueError('valor inserido excede o limite permitido de R$100')
    sorteadas = input('digite as duas fichas: ').lower()
    resultado = fichas[sorteadas] * valor
    resultado = int(resultado) if int(resultado) == resultado else resultado
    print(resultado)


if __name__ == '__main__':
    main()
