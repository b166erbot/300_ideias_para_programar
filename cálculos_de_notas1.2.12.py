def main():
    n1, n2, n3, n4 = (float(a) for a in input('notas: ').split())
    print(f'média: {(n1 + n2 * 2 + n3 * 3 + n4 * 4) / 10:0.1f}')


if __name__ == '__main__':
    main()
