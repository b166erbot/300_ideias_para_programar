from os import system as sy


def main():
    nome = input('Nome completo: ')
    endereço = input('Endereço: ')
    cep = input('Cep: ')
    telefone = input('Telefone: ')
    sy('clear')
    print(nome, endereço, cep + ' - ' + telefone, sep='\n')


if __name__ == '__main__':
    main()
