def main():
    n = int(input('número: ')) + 1
    soma = sum([((1 + a / n - a) + (n - a / 1 + a)) for a in range(n)])
    print(soma)


if __name__ == '__main__':
    main()
