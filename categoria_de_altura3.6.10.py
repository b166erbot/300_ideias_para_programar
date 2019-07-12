def main():
    altura = float(input('digite a altura: ').replace(',', '.'))
    if altura < 1.60:
        print('baixinho')
    elif 1.60 <= altura <= 1.85:
        print('altura normal')
    else:
        print('faz frio aí em cima?')


if __name__ == '__main__':
    main()
