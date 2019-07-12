def main():
    a, b, c = (float(a) for a in input('digite os lados: ').split())
    if all((a + b >= c, b + c >= a, c + a >= b)):
        if a == b == c:
            print('equilátero')
        elif a == b or b == c or c == a:
            print('isóceles')
        elif a != b != c:
            print('escaleno')
    else:
        print('não forma um triangulo')


if __name__ == '__main__':
    main()
