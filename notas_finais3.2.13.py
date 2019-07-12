def main():
    pesos = (2, 3)
    notas = (float(a) for a in input('digite as notas: ').split())
    média = sum(map(lambda x: x[0] * x[1], zip(notas, pesos))) / 5
    temp = média - int(média)
    if 0 <= temp <= 0.25:
        média = int(média)
        print('primeira')
    elif temp <= 0.5:
        média = int(média) + 0.5
        print('segunda')
    else:
        média = int(média) + 1
    print(média)


if __name__ == '__main__':
    main()
