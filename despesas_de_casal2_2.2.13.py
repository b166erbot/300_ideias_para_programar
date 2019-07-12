def main():
    marido = float(input('despesas do marido: ').replace(',', '.'))
    esposa = float(input('despesas da esposa: ').replace(',', '.'))
    total = marido + esposa
    marido_pa = total / 100 * 60
    esposa_pa = total / 100 * 40
    marido_p = marido * 100 / total
    esposa_p = esposa * 100 / total
    forma_tabelas = '{: <17}|{: <7}|{: <7}|{: <7}'
    forma_separador = '{: <17}|{: >7}|{: >7}|{: >7}'
    forma_itens = '{: <17}|{: >7.2f}|{: >7.2f}|{: >7.2f}'
    forma_saldo = '{: <17}|{: >7.2f}|{: >7.2f}|'
    print(forma_tabelas.format('item', 'marido', 'esposa', 'total'))
    print(forma_separador.format('=' * 17, '=' * 7, '=' * 7, '=' * 7))
    print(forma_itens.format('despesas à pagar', marido, esposa, total))
    print(forma_itens.format('% pago', marido_p, esposa_p, 100))
    print(forma_itens.format('valor devido', marido_pa, esposa_pa, total))
    print(forma_saldo.format('saldo', marido - marido_pa, esposa - esposa_pa))


if __name__ == '__main__':
    main()
