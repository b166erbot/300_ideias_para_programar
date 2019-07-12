def main():
    numeros = (float(a) for a in input('digite três números: '))
    media = sum(numeros) / len(numeros)
    print(media)


if __name__ == '__main__':
    main()
