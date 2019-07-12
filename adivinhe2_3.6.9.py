from random import randint

def main():
    máquina = randint(1, 5)
    for a in range(2):
        usuário = int(input('jogo do adivinha. escolha um número de 1/5: '))
        print('acertou!' if usuário == máquina else 'errou')



if __name__ == '__main__':
    main()
