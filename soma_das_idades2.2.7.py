def fatorial(n):
    if n <= 0:
        return n
    return n + fatorial(n-1)


def main():
    soma = fatorial(int(input('Idade: ')))
    print(f'a soma de todas as idades que você já teve é de {soma}')


if __name__ == '__main__':
    main()
