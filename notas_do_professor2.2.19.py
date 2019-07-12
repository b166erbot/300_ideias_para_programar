def main():
    entrada = input('Digite as duas notas: ').split()
    primeira = sum((int(a) * b for a, b in zip(entrada, (1, 2)))) / 3
    entrada = float(input('Digite a próxima nota: '))
    média = (primeira * 2 + entrada * 8) / 10
    print(f"média: {média:0.1f}")


if __name__ == '__main__':
    main()
