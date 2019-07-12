def main():
    entrada = [int(a) for a in input('Digite as duas notas: ').split()]
    if not all((0 <= a <= 10 for a in entrada)):
        raise ValueError('notas fora do intervalo 0 / 10')
    primeira = sum((a * b for a, b in zip(entrada, (1, 2)))) / 3
    entrada = float(input('Digite a próxima nota: '))
    if not 0 <= entrada <= 10:
        raise ValueError('nota fora do intervalo 0 / 10')
    média = (primeira * 2 + entrada * 8) / 10
    print(f"média: {média:0.1f}")


if __name__ == '__main__':
    main()
