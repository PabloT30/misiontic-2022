# Reto # 1 - Semana 1-2
# Tema: Empacadora de suministros
# Autor: Pablo Jose Torres Mojica
# Cohorte: 18/05/2021
# Objetivo: Determinar el tamaño adecuado de la bolsa
# para un grupo de suministros dada la cantidad
# de los mismos.


def get_supply_group():
    supply_group = {'Laces': abs(int(input()))}
    supply_group['Tacks'] = supply_group['Laces'] * 2 + 4
    supply_group['Screws'] = (supply_group['Laces'] + supply_group['Tacks']) // 5

    return supply_group


def get_bag_size(supply_group):
    if 0 <= supply_group['Screws'] <= 20:
        return 'uno'
    elif supply_group['Screws'] <= 30:
        return 'dos'
    elif supply_group['Screws'] <= 50:
        return 'tres'
    else:
        return 'cuatro'


def main():
    supply_group = get_supply_group()
    supply_group['Bag Size'] = get_bag_size(supply_group)
    print(f"{supply_group['Laces']} {supply_group['Tacks']} {supply_group['Screws']}")
    print(f"{supply_group['Bag Size']}")


if __name__ == '__main__':
    main()
