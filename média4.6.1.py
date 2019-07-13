def main():
    entrada = [int(a) for a in input('digite 20 números: ').split()]
    print(sum(entrada) / len(entrada))


if __name__ == '__main__':
    main()
