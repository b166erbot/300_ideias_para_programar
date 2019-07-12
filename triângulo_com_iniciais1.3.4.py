from os import get_terminal_size as get

def main():
    colunas, linhas = get()
    for a in range(0, linhas, 2):
        if a != linhas // 2:
            print(f'/{" " * a}\\'.center(colunas))
        else:
            t = (a - 7) // 2
            t2 = t + (1 if (a - 7) / 2 != (a - 7) // 2 else 0)
            print(f"/{' ' * t + 'anonimo' + ' ' * t2}\\".center(colunas))
    print(('-' * (a + 2)).center(colunas))
    input('digite ENTER para sair.')


if __name__ == '__main__':
    main()
