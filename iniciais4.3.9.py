def main():
    entrada = input('digite um nome: ').split()
    print(' '.join([a[0] for a in entrada]))


if __name__ == '__main__':
    main()
