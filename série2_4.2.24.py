def main():
    n = int(input('número: ')) + 1
    soma = sum([(1 / a) for a in range(2, n)])
    print(soma + 1)


if __name__ == '__main__':
    main()
