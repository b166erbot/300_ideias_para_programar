def main():
    tabu = int(input('qual tabuada deseja ver 1/9: '))
    for vezes in range(1, 11):
        print(f"{tabu} * {vezes} = {tabu * vezes}")


if __name__ == '__main__':
    main()
