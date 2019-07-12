from operator import sub, mul, floordiv


def main():
    ns = [float(a) for a in input('Digite dois números: ').split()]
    soma = float(sum(ns))
    diferença = float(sub(*ns))
    produto = float(mul(*ns))
    quociente = floordiv(*ns)
    print(f'soma: {soma:0.2f} diferença: {diferença:0.2f} '
         f'produto: {produto:0.2f} quociente: {quociente:0.2f}')


if __name__ == '__main__':
    main()
