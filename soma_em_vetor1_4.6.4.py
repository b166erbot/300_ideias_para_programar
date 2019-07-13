from operator import add
from random import randint


def main():
    vetor1 = [randint(0, 10) for a in range(15)]
    vetor2 = [randint(0, 10) for a in range(15)]
    vetor3 = list(map(add, vetor1, vetor2))
    forma = 'vetor1 {}\nvetor2 {}\nvetor3 {}'
    print(forma.format(vetor1, vetor2, vetor3))


if __name__ == '__main__':
    main()
