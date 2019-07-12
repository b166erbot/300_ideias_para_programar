def main():
    a, b, c, d, e, f = '═║╔╗╚╝'
    linhas = [input('frase: ') for a in range(3)]
    for frase in linhas:
        print(f'{c}{a * (len(frase) + 2)}{d}')
        print(f'{b} {frase} {b}')
        print(f'{e}{a * (len(frase) + 2)}{f}')


if __name__ == '__main__':
    main()
