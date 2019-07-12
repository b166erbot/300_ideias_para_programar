def main():
    alunos = ['ALINE', 'MÁRIO', 'SÉRGIO', 'SHIRLEY']
    notas = [9.0, 'DEZ', 4.5, 7.0]
    print('ALUNO(A)             NOTA')
    print('========             ====')
    for aluno, nota in zip(alunos, notas):
        print(f'{aluno: <21}{nota}')


if __name__ == '__main__':
    main()
