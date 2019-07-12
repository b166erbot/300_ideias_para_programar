def main():
    pol = 2.54
    cen = int(input('centímetros: '))
    var = int(input('variação: '))
    for a in range(cen, cen + 101, var):
        print(f"|{a * pol: >{len(str(cen)) + 7}}|")


if __name__ == '__main__':
    main()
