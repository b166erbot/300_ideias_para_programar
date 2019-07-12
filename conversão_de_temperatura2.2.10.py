def main():
    temperatura = float(input('fahrenheit: ').replace(',', '.'))
    c = (temperatura - 32) * 5 / 9
    print(f'celsius: {c:0.2f}')


if __name__ == '__main__':
    main()
