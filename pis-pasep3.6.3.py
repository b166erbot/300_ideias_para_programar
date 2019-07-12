from re import compile
from operator import mul


def main():
    pisPasep = compile(r'^\d{10}')
    nMult = (3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
    numeros = input('digite o número pis/pasep: ')
    numeros = (int(a) for a in pisPasep.findall(numeros)[0])
    resultado = 11 - (sum(map(lambda x: mul(*x), zip(numeros, nMult))) % 11)
    resultado = 0 if resultado == 10 else resultado
    print(resultado)



if __name__ == '__main__':
    main()
