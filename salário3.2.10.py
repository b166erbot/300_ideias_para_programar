def main():
    valor = float(input('valor: '))
    horas = float(input('horas extras: '))
    valor += (valor / 176) * horas * 1.5
    inss = valor * 10 / 100
    inss = inss if inss <= 150 else 150
    print(f"R${valor - inss:0.2f}")


if __name__ == '__main__':
    main()
