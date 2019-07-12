def entrada(texto):
    try:
        temp = int(input(texto)) * 10000
    except ValueError:
        temp = 0
    return temp

def main():
    cinco = entrada('quantidade de madeiras 5 metros: ')
    quatro = entrada('quantidade de madeiras 4 metros: ')
    tres = entrada('quantidade de madeiras para 3 metros: ')
    pedaços = 0
    sobra = 0
    for a in (cinco, quatro, tres):
        resto = a % 45
        sobra += resto
        pedaços += (a - resto) // 45
    print(f'pedaços = {pedaços}, sobra = {sobra} centímetros.')


if __name__ == '__main__':
    main()
