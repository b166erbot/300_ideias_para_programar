from re import compile
from operator import add, sub, mul, floordiv


def main():
    operators = {'+': add, '-': sub, '*': mul, '/': floordiv}
    separar = compile(r'^ *(-?\d+\.?\d*) *([\+\-\*\/]) *(-?\d+\.?\d*)')
    erroDivisãoZero = compile(r'^ *-?\d+.?\d* */ *0+\.?0*')
    conta = input('digite a conta aritimética: ')
    itens = separar.findall(conta)
    if len(itens[0]) != 3:
        raise ValueError('a algo de errado com sua conta')
    elif erroDivisãoZero.findall(conta):
        raise ZeroDivisionError('erro de divisão por zero')
    a, b, c = itens[0]
    a, c = float(a), float(c)
    resultado = operators[b](a, c)
    resultado = int(resultado) if int(resultado) == resultado else resultado
    print(resultado)


if __name__ == '__main__':
    main()
