def main():
    nota = float(input('informe uma nota: '))
    if 9 <= nota <= 10:
        print('SS(superior)')
    elif 7 <= nota <= 8.9:
        print('MS(médio superior)')
    elif 5 <= nota <= 6.9:
        print('MM(médio)')
    elif 3 <= nota <= 4.9:
        print('MI(médio inferior)')
    elif 0.1 <= nota <= 2.9:
        print('II(inferior)')
    else:
        print('SR(sem rendimento)')


if __name__ == '__main__':
    main()
