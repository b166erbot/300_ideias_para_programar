def main():
    for ponto in range(101):
        fharenheit = ponto / 9 * 5 + 32
        print(f"celsius: {ponto}, fahrenheit: {fharenheit:0.1f}")


if __name__ == '__main__':
    main()
