def main():
    marido = float(input('despesas do marido: '))
    esposa = float(input('despesas da esposa: '))
    total = marido + esposa
    metade = total / 2
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
    print(forma_itens.format('valor devido', metade, metade, total))
    print(forma_saldo.format('saldo', marido - metade, esposa - metade))


if __name__ == '__main__':
    main()
