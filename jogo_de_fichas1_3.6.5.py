def main():
    fichas = {'branca branca': 0, 'branca preta': 0.5, 'preta branca': 1,
              'preta preta': 2}
    sorteadas = input('digite as duas fichas: ').lower()
    print(fichas[sorteadas])


if __name__ == '__main__':
    main()
