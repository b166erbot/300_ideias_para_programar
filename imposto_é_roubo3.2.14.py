def main():
    salario = float(input('salário: ').replace(',', '.')) - 1200
    if salario > 0:
        primeiro = salario if salario <= 1299 else 1299
        roubo1 = primeiro / 100 * 10
        salario -= primeiro if salario > 0 else 0
        segundo = salario if salario <= 2499 else 2499
        roubo2 = segundo / 100 * 15
        salario -= segundo if salario > 0 else 0
        roubo3 = salario / 100 * 20
    else:
        roubo1, roubo2, roubo3 = 0, 0, 0
    print(f'soma dos impostos = {sum((roubo1, roubo2, roubo3)):0.2f}')


if __name__ == '__main__':
    main()
