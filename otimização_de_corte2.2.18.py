def main():
    tábuas = []
    nova_entrada = True
    while nova_entrada:
        a = float(input('tamanho da tábua: ')) * 10000
        b = int(input(f'quantidade de tábuas: '))
        tábuas.append((a, b))
        if input('nova entrada? [s/n]: ').lower() == 's':
            nova_entrada = True
        else:
            nova_entrada = False
    pedaços = 0
    sobra = 0
    for a,b  in tábuas:
        temp = a * b
        resto = temp % 45
        sobra += resto
        pedaços += (temp - resto) // 45
    print(f'pedaços = {pedaços}, sobra = {sobra} centímetros.')


if __name__ == '__main__':
    main()
