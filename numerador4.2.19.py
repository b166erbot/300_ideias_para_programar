def main():
    inicio = int(input('inicio: '))
    final = int(input('final: '))
    distância = list(range(inicio, final + 1))
    chunk = lambda l, n: [l[i:i+n] for i in range(0, len(l), n)]
    distância = chunk(distância, 10)
    for lista in distância:
        print(*lista)


if __name__ == '__main__':
    main()
