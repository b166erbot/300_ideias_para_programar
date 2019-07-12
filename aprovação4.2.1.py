def main():
    disciplina = input('disciplina: ')
    nota = float(input('nota: ').replace(',', '.'))
    while 0 < nota <= 10:
        print('passou' if nota >= 7 else 'não passou')
        disciplina = input('disciplina: ')
        nota = float(input('nota: ').replace(',', '.'))


if __name__ == '__main__':
    main()
