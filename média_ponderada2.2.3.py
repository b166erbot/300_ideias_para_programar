def main():
    entradas = (float(a) for a in input('números: ').split())
    temp = ((número * entrada) for número, entrada in enumerate(entradas, 1))
    média = sum(temp) / 10
    print(média)


if __name__ == '__main__':
    main()
