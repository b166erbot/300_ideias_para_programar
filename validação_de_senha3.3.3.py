from getpass import getpass

def main():
    s = 'senha predefinida'
    s2 = getpass('digite a senha: ')
    if s == s2:
        print('Acesso autorizado')
    else:
        print('Acesso negado')


if __name__ == '__main__':
    main()
