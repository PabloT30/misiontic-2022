# Reto # 3 - Semana 5
# Tema: Disfraces creativos
# Autor: Pablo Jose Torres Mojica
# Cohorte: 18/05/2021
# Objetivo: Contar el número de disfraces repetidos encuentran
# en el camino a la fiesta en orden de aparición.

def get_seen_costumes():
    return input().split(" ")


def main():
    costumes = get_seen_costumes()
    seen_costumes = []
    number_of_occurrences = []
    last_costume = costumes[0]
    seen_costumes.append(costumes[0])
    counter = 0

    for costume in costumes:
        if costume == last_costume:
            counter += 1
        else:
            number_of_occurrences.append(str(counter))
            counter = 0
            seen_costumes.append(costume)
            counter += 1
            last_costume = costume
    else:
        number_of_occurrences.append(str(counter))

    print(" ".join(seen_costumes))
    print(" ".join(number_of_occurrences))


if __name__ == '__main__':
    main()
