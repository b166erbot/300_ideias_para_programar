def main():
    ano = int(input('digite um ano: '))
    print('o ano é bissexto' if ano % 4 == 0 else 'o ano não é bissexto')


if __name__ == '__main__':
    main()
