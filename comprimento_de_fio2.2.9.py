def main():
    a, b = (float(a) ** 2 * 10000 for a in input('lados: ').split())
    c = a + b
    print(f'Quantidade de fio a ser comprado: {c ** 0.5:0.2f} centímetros.')


if __name__ == '__main__':
    main()
