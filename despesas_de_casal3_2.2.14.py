def main():
    marido = float(input('despesas do marido: ').replace(',', '.'))
    esposa = float(input('despesas da esposa: ').replace(',', '.'))
    marido_r = float(input('renda do marido: ').replace(',', '.'))
    esposa_r = float(input('renda da esposa: ').replace(',', '.'))
    total_r = marido_r + esposa_r
    total = marido + esposa
    marido_p = marido * 100 / total
    esposa_p = esposa * 100 / total
    marido_pa = (100 * marido_r / total_r) * (total / 100)
    esposa_pa = (100 * esposa_r / total_r) * (total / 100)
    forma_tabelas = '{: <17}|{: <7}|{: <7}|{: <7}'
    forma_separador = '{: <17}|{: >7}|{: >7}|{: >7}'
    forma_itens = '{: <17}|{: >7.2f}|{: >7.2f}|{: >7.2f}'
    forma_saldo = '{: <17}|{: >7.2f}|{: >7.2f}|'
    print(forma_tabelas.format('item', 'marido', 'esposa', 'total'))
    print(forma_separador.format('=' * 17, '=' * 7, '=' * 7, '=' * 7))
    print(forma_itens.format('despesas à pagar', marido, esposa, total))
    print(forma_itens.format('renda', marido_r, esposa_r, total_r))
    print(forma_itens.format('% pago', marido_p, esposa_p, 100))
    print(forma_itens.format('valor devido', marido_pa, esposa_pa, total))
    print(forma_saldo.format('saldo', marido - marido_pa, esposa - esposa_pa))


if __name__ == '__main__':
    main()
