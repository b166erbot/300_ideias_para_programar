def main():
    pessoa = input('digite um tipo de pessoa F/J: ').upper()
    if pessoa == 'F':
        print('pessoa física')
    elif pessoa == 'J':
        print('pessoa jurídica')
    else:
        print('tipo de pessoa inválido')


if __name__ == '__main__':
    main()
