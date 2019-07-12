from os import system as sy
from pyxhook import HookManager


class Constructor:
    tela = 0
    texto = ('FOTOSSÍNTESE',
             ('A água e os sais minerais absorvidos pelas raízes sobem através '
              'dos vasos lenhosos do caule e chegam às folhas.'),
             ('Nas folhas, existe uma substância verde, a clorofila, que '
              'absorve a energia luminosa do sol. Ao mesmo tempo, por meio dos'
              ' estômatos presentes nas folhas, a planta absorve gás carbônico'
              ' do ar.'),
             ('Usando a energia solar, o gás carbônico e o hidrogênio contido'
              ' na água retirada do solo, após complicadas reações químicas,'
              ' a planta produz açúcares (glicose).'))

    def __init__(self):
        sy('clear')
        print('FOTOSSÍNTESE')
    def __call__(self, event):
        if event.Key == 'Left' and event.MessageName == 'key up':
            sy('clear')
            if self.tela - 1 in range(len(self.texto)):
                self.tela -= 1
                print(self.texto[self.tela])
            else:
                print(self.texto[0])
                print('\naviso: não tem como retroceder mais que o início')
        elif event.Key == 'Right' and event.MessageName == 'key up':
            sy('clear')
            if self.tela + 1 in range(len(self.texto)):
                self.tela += 1
                print(self.texto[self.tela])
            else:
                print(self.texto[-1])
                print('\naviso: não tem como avançar mais que o final')


def main():
    onKeyPress = Constructor()
    keyboard = HookManager()
    keyboard.KeyDown = onKeyPress
    keyboard.KeyUp = onKeyPress
    keyboard.HookKeyboard()
    keyboard.start()


if __name__ == '__main__':
    main()
