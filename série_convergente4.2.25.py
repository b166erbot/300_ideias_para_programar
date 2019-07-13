def main():
    n = int(input('número limite: '))
    soma = sum([(1 / a) for a in range(2, n + 1, 2)]) + 1
    print(soma)


if __name__ == '__main__':
    main()
