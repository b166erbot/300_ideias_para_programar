def main():
    números = (int(a) for a in input('digite três números: ').split())
    print(f"o maior é o {max(números)}")


if __name__ == '__main__':
    main()
