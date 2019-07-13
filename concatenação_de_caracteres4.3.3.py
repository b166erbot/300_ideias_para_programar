def main():
    entrada = input('digite vários números de 32 à 254: ').split()
    entrada = [int(a) for a in entrada]
    while any(map(lambda x: x not in range(32, 255), entrada)):
        errados = [(a, b) for a, b in enumerate(entrada)
                   if b not in range(32, 255)]
        for index, número in errados:
            print(f'número fora do intervalo de 32 à 254: {número}')
            correção = int(input('digite um número para corrigi-lo: '))
            while not correção in range(32, 255):
                print(f'número fora do intervalo de 32 à 254: {correção}')
                correção = int(input('digite um número para corrigi-lo: '))
            entrada[index] = correção
    string = ''.join([chr(a) for a in entrada])
    print(string)



if __name__ == '__main__':
    main()
