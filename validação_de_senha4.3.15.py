def main():
    senha = 'sei lá'
    for tentativa in range(1, 4):
        senha2 = input('digite a senha: ')
        if senha == senha2:
            print('logado.')
            break


if __name__ == '__main__':
    main()
