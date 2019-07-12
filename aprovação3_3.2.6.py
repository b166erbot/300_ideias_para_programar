def main():
    disciplina = input('digite o nome da disciplina: ')
    nota = float(input('digite sua respectiva nota: ').replace(',', '.')) * 0.5
    aulas = int(input('digite a quantidade de áulas: '))
    faltas = int(input('digite a quantidade de faltas: '))
    if nota not in range(21):
        raise ValueError(
            'sua nota não é válida. está fora do intervalo permitido.')
    elif faltas * 100 / aulas >= 75:
        print('você foi reprovado.')
    else:
        if 5 <= nota <= 10:
            print(f'você foi aprovado na disciplina {disciplina}')
        elif 4 <= nota <= 4.5:
            print(f'você ficou de recuperação  na disciplina {disciplina}')
        else:
            print(f'você reprovou na disciplina {disciplina}')


if __name__ == '__main__':
    main()
