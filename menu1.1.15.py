from os import system as sy
from time import sleep


class Cadastro:
    def __init__(self):
        self.itens = ['Fim', 'Incluir', 'Alterar', 'Excluir', 'Consultar']
        self.dicio = dict(enumerate(
            (exit, self.incluir, self.alterar, self.excluir,
             self.consultar)
            ))

    def selecionar(self):
        while True:
            sy('cls | clear')
            print('Cadastro de Clientes\n')
            for num, item in enumerate(self.itens):
                print(f'{num} - {item}')
            try:
                opcao = int(input('\nOpção: '))
            except:
                continue
            print()
            if opcao in self.dicio:
                self.dicio[opcao]()
            else:
                print('Opção inválida')
                sleep(1)

    def incluir(self):
        with open('cadastros.txt', 'a') as file:
            file.write(input('Nome do cliente: ') + '\n')

    def alterar(self):
        nome = input('Nome do cliente: ')
        novo_nome = input('Nome para ser alterado: ')
        with open('cadastros.txt') as file:
            linhas = (a for a in file.readlines())
        with open('cadastros.txt', 'w') as file:
            for linha in linhas:
                file.write(novo_nome if linha == nome else linha)

    def excluir(self):
        nome = input('Nome do cliente: ')
        with open('cadastros.txt') as file:
            linhas = (a for a in file.readlines())
        with open('cadastros.txt', 'w') as file:
            file.write('')
        with open('cadastros.txt', 'a') as file:
            for linha in linhas:
                if nome != linha.strip():
                    file.write(linha + '\n')

    def consultar(self):
        nome = input('Nome do cliente: ')
        with open('cadastros.txt') as file:
            linhas = (a for a in file.readlines())
        for linha in linhas:
            if nome in linha:
                print(linha)
        input('Precione algo para continuar.')


def main():
    cadastro = Cadastro()
    cadastro.selecionar()


if __name__ == '__main__':
    main()
