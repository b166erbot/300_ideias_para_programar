from math import exp, log, sqrt, pow as pow2


def main():
    n = int(input('Digite um número: '))
    print(f'quadrado: {pow2(n, 2):0.2f} raiz: {sqrt(n):0.2f} '
          f'logaritmo: {log(n):0.2f} exponencial: {exp(n):0.2f}')


if __name__ == '__main__':
    main()
