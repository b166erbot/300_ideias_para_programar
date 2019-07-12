def main():
    entrada = input('digite uma frase: ')
    print(entrada[:len(entrada) // 2], entrada[len(entrada) // 2:], sep='\n')


if __name__ == '__main__':
    main()
