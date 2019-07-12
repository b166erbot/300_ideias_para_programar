def main():
    tempo = 100
    livre = tempo % 6
    materia_tempo = int((tempo - livre) / 6)
    print(f'tempo para cada matéria: {materia_tempo}\ntempo livre: {livre}')


if __name__ == '__main__':
    main()
