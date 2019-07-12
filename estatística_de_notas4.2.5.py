def main():
    notas = []
    for a in range(5):
        nota = float(input('digite uma nota: ').replace(',', '.'))
        if not 0 <= nota <= 10:
            raise ValueError('notas fora do intervalo 0/10')
        notas.append(nota)
    abaixo_de_5 = tuple(filter(lambda x: x < 5, notas))
    media = sum(notas) / len(notas)
    print(f"quantidade: {len(notas)}, média: "
          f"{media}, abaixo de 5: {abaixo_de_5}")


if __name__ == '__main__':
    main()
