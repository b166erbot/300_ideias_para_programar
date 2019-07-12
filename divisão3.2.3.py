def main():
    dividendo = int(input('escreva o dividendo: '))
    divisor = int(input('escreva o divisor: '))
    if divisor != 0:
        print(dividendo / divisor)
    else:
        print('erro de divisão por zero.')


if __name__ == '__main__':
    main()
