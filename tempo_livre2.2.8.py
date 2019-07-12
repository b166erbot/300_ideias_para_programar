def main():
    tempo = int(input('tempo: '))
    diciplinas = int(input('número de disciplinas: '))
    livre = tempo % disciplinas
    materia_tempo = int((tempo - livre) / diciplinas)
    print(f'tempo para cada matéria: {materia_tempo}\ntempo livre: {livre}')


if __name__ == '__main__':
    main()
