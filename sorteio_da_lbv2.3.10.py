def main():
    entrada = input('digite dois prémios: ').split()
    entrada = [a.split('.')[1] for a in entrada]
    print(entrada[0] + '.' + entrada[1])


if __name__ == '__main__':
    main()
