def main():
    entrada = input('digite uma frase: ')
    while entrada:
        print(entrada[::-1])
        entrada = input('digite uma frase: ')


if __name__ == '__main__':
    main()
