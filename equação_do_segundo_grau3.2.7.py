def equaçãoSegundoGrau(a, b, c):
    delta = b ** 2 -4 * a * c
    if delta < 0:
        print('a equação não tem solução real.')
    elif delta > 0:
        x1 = (- b + delta ** 0.5) / (2 * a)
        x2 = (- b - delta ** 0.5) / (2 * a)
        print(x1, x2)
    else:
        x = - b / (2 * a)
        print(x)


def main():
    entradas = (int(a) for a in input('digite os valores a, b, c: ').split())
    equaçãoSegundoGrau(*entradas)


if __name__ == '__main__':
    main()
