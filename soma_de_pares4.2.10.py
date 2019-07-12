def main():
    inicial = int(input('número inicial: '))
    final = int(input('número final: ')) + 1
    print(sum((a for a in range(inicial, final) if a % 2 == 0)))


if __name__ == '__main__':
    main()
