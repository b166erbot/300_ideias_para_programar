def main():
    números = []
    número = int(input('número: '))
    while número != 0:
        números.append(número)
        número = int(input('número: '))
    print(max(números))


if __name__ == '__main__':
    main()
