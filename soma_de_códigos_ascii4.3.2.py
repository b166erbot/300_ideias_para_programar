def main():
    string = input('digite uma frase: ')
    print(sum([ord(a) for a in string]))


if __name__ == '__main__':
    main()
