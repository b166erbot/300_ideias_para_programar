def main():
    frases = ('pense em um número', 'multiplique por 2', 'some + 6',
              'divida por 2')
    for frase in frases:
        print(frase)
        input('aperte enter para continuar.')
    número = ((int(input('quanto deu?: ')) * 2) + 6) / 2
    print(f'você pensou no número {número}!')


if __name__ == '__main__':
    main()
