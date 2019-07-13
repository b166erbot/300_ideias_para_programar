from random import randint
from operator import add


def main():
    vetor1 = [(randint(0, 10), randint(0, 10)) for a in range(10)]
    vetor2 = [a + b for a, b in vetor1]
    forma = 'vetor1 {}\nvetor2 {}'
    print(forma.format(vetor1, vetor2))


if __name__ == '__main__':
    main()
