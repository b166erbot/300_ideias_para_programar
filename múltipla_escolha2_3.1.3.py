from collections import namedtuple


def main():
    questões = namedtuple(
        'questões',
        ('questão', 'opcao1', 'opcao2', 'opcao3', 'opcao4', 'correta'))
    questão1 = questões(
        'qual dessas alternativas cria uma tabela roupas?',
        '1 - create desk roupas',
        '2 - create roupas table',
        '3 - create table roupas',
        '4 - insert into roupas values="create",',
        '3')
    questão2 = questões(
        'qual comando do sql deleta uma tabela?',
        '1 - drop table nomeDaTabela',
        '2 - delete table nomeDaTabela',
        '3 - remove table nomeDaTabela',
        '4 - replace table nomeDaTabela None',
        '1')
    print('qual questão você deseja responder?')
    opção = input('1 - criar uma tabela, 2 - deleta uma tabela: ')
    questão = (questão1 if opção == '1' else questão2)
    for a in questão[:-1]:
        print(a)
    opção = input('opção: ')
    if opção == questão[-1]:
        print('acertou!')
    else:
        print('errou.')


if __name__ == '__main__':
    main()
