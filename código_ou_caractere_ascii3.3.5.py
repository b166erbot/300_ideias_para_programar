def main():
    opção = int(input('ascii ou código 1/2: '))
    if opção == 1:
        print(chr(int(input('digite um número entre 1 - 255: '))))
    else:
        print(ord(input('digite um character: ')))


if __name__ == '__main__':
    main()
