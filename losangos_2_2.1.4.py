def main():
    c = int(input('em qual coluna devo imprimir os losangos?: '))
    distancia = list(range(1, 10, 2)) + list(range(7, 0, -2))
    losango = ('\n').join(' ' * c + ('*' * a).center(10) * 2 for a in distancia)
    print(losango)


if __name__ == '__main__':
    main()
