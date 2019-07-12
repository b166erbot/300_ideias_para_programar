def main():
    notas = [float(a) for a in input('Digite às 2 notas: ').split()]
    pesos = (2, 3)
    final = 0
    print(sum(map(lambda x: x[0] * x[1], zip(notas, pesos))) / 5)


if __name__ == '__main__':
    main()
