from random import randint


def main():
    números = [(a, randint(0, 1000)) for a in range(100)]
    maior, menor = (0, 0), (0, float('inf'))
    for a in números:
        if a[1] > maior[1]:
            maior = a
        if a[1] < menor[1]:
            menor = a
    forma = "maior, index: {} - {}; menor, index: {} - {}"
    print(forma.format(*maior[::-1], *menor[::-1]))


if __name__ == '__main__':
    main()
