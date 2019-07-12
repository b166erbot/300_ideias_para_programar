def main():
    print('qual dessas alternativas cria uma tabela roupas?')
    print('1 - create desk roupas', '2 - create roupas table', sep='\n')
    print('3 - create table roupas', '4 - insert into roupas values="create",',
          sep='\n')
    opção = input('opção: ')
    if opção == '3':
        print('acertou!')
    else:
        print('eu acho que alguém precisa estudar um pouquinho mais sql.')


if __name__ == '__main__':
    main()
