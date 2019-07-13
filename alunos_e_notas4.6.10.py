def main():
    bancoDeDados = []
    inserir = True
    while inserir:
        aluno, nota = input('digite o nome do aluno e a nota: ').split()
        bancoDeDados.append((aluno, float(nota)))
        inserir = (True if input('inserir mais notas? s/n: ').lower() == 's'
                   else False)
    for aluno, nota in bancoDeDados:
        print(f"aluno: {aluno}, nota: {nota}")
    print(f'quantidade de alunos = {len(bancoDeDados)}')
    média = sum([a[1] for a in bancoDeDados]) / len(bancoDeDados)
    print(f"média das notas: {média}")


if __name__ == '__main__':
    main()
