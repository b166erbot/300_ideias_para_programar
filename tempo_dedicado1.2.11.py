def main():
    min = (365 // 7) * 6 * 5
    minutos = min % 60
    horas = min // 60
    print(f'uma pessoa dedicou em um ano {horas:02}:{minutos:02}'
          ' horas lendo livros.')


if __name__ == '__main__':
    main()
