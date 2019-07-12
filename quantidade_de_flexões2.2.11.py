def fatorial(n):
    if n == 1:
        return n
    return n + fatorial(n - 1)


def main():
    fatorial = fatorial(int(input('Flexões: ')))
    print(f'Total de flexões: {fatorial}')


if __name__ == '__main__':
    main()
