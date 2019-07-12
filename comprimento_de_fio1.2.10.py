def main():
    a, b = 11.5 ** 2 * 10000, 6.3 ** 2 * 10000
    c = a + b
    print(f'Quantidade de fio a ser comprado: {c ** 0.5:0.2f} centímetros.')


if __name__ == '__main__':
    main()
