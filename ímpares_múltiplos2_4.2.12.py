def main():
    final = int(input('número inicial: ')) + 1
    inicial = int(input('número final: '))
    print(*(a for a in range(inicial, final, -1) if a % 3 == 0))


if __name__ == '__main__':
    main()
