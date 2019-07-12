def main():
    notas = ((90, 101), (75, 90), (50, 75), (40, 50), (0, 40))
    conceitos = dict(zip(notas, ('A', 'B', 'C', 'D', 'E')))
    nota = float(input('digite uma nota: ').replace(',', '.'))
    if nota > 100 or nota < 0:
        raise ValueError('nota fora do intervalo permitido 0/100')
    a = next(filter(lambda x: x[0] <= nota <= x[1], notas))
    print(conceitos[a])


if __name__ == '__main__':
    main()
