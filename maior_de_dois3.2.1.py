def main():
    a, b = (int(a) for a in input('digite dois números: ').split())
    if a != b:
        print(f"o maior é {max((a, b))}")
    else:
        print('iguais')


if __name__ == '__main__':
    main()
