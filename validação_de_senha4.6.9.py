def main():
    bancoDeDados = [('nome', 'senha'), ('asdf', 'fdsa'), ('qwer', 'rewq')]
    for a in range(3):
        nome = input('login: ')
        senha = input('senha: ')
        if (nome, senha) in bancoDeDados:
            print('bem vindo!')
            break
        else:
            print('senha e/ou password errados')


if __name__ == '__main__':
    main()
