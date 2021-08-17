# Reto # 2 - Semana 2-3
# Tema: Elecciones problemáticas
# Autor: Pablo Jose Torres Mojica
# Cohorte: 18/05/2021
# Objetivo: Definir el empate de las elecciones de personero del colegio
# San Manuel de Málaga por medio de un algoritmo novedoso.

class Candidate:
    n = 0

    def __new__(cls, *args, **kwargs):
        if cls.n <= 2:
            cls.n += 1
            return object.__new__(cls)

    def __init__(self, name):
        self.name = name
        self.choice = ''
        self.votes = 0

    def __repr__(self):
        return f"Candidate({self.name}, {self.choice})"

    def __str__(self):
        return f"Candidate {self.name} chose '{self.choice}' to compete."

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_choice(self):
        return self.choice

    def set_choice(self, choice):
        self.choice = choice

    def get_votes(self):
        return self.votes

    def add_vote(self):
        self.votes += 1


def main():
    laura = Candidate("Laura")
    laura.set_choice(input())

    carlos = Candidate("Carlos")
    carlos.set_choice(input())

    students_initials = input()
    elections_results = []

    for initial in students_initials:

        if initial in laura.get_choice():
            laura.add_vote()
        if initial in carlos.get_choice():
            carlos.add_vote()

        if laura.get_votes() == carlos.get_votes():
            elections_results.append('E')
        elif laura.get_votes() > carlos.get_votes():
            elections_results.append('L')
        else:
            elections_results.append('C')
    else:
        print("".join(elections_results))


if __name__ == '__main__':
    main()
