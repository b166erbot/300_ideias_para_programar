def main():
    disciplina = input('digite o nome da disciplina: ')
    nota = float(input('digite sua respectiva nota: ')) * 0.5
    if 5 <= nota <= 10:
        print(f'você foi aprovado na disciplina {disciplina}')
    elif 4 <= nota <= 4.5:
        print(f'você ficou de recuperação  na disciplina {disciplina}')
    else:
        print(f'você reprovou na disciplina {disciplina}')


if __name__ == '__main__':
    main()
