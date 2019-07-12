import re

def main():
    formato = re.compile(r'^\d{2}/\d{2}/\d{4}$')
    dM = re.compile(r'^(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/\d{4}$')
    data = input('digite uma data no formato dd/mm/aaaa: ')
    if bool(formato.findall(data)) == False:
        return print('a data não está no formato certo')
    elif bool(dM.findall(data)) == False:
        return print('a data não está com os dias ou meses corretos')
    print('a data está correta')


if __name__ == '__main__':
    main()
