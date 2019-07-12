def main():
    print('celsius       fahrenheit')
    print('-' * 24)
    for a in range(1, 11):
        print(f'{a:<2}            {(a * 9) / 5 + 32}')
    print('-' * 24)


if __name__ == '__main__':
    main()
