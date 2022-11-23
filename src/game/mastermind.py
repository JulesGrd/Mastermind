from random import randint

LISTE_COULEURS = ("B" , "J" , "V" , "R" , "N")

class Mastermind:

    def __init__(self, tries=8):
        self.tries = tries
        self.guesses = 0
        self.solution = []

    def generate_solution(self):
        self.solution = [LISTE_COULEURS[randint(0, len(LISTE_COULEURS))] for _ in range(4)]

    def compare(self, guess):
        retour = []
    
        for i in range(len(guess)):
            if self.solution[i] == guess[i]:
                retour.append("o")
            elif self.solution[i] in guess:
                retour.append("-")
            else:
                retour.append("x")
            
        return retour

    def test_win(self, guess):
        return self.compare(guess) == ["o", "o", "o", "o"]

    def ask_guess(self):
        guess = input('Proposition (ex : BJNJ) :')

        assert len(guess) == 4, "La proposition doit être de 4 couleurs"
        assert all([c in LISTE_COULEURS for c in guess]), "La proposition doit être composée de couleurs valides" + str(LISTE_COULEURS)

        return [guess[i] for i in range(4)]

    def play(self):
        self.generate_solution()

        while self.guesses < self.tries:
            guess = self.ask_guess()

            self.guesses += 1
            print(self.compare(guess))

            print("-----------------------------------------------")


            if self.test_win(guess):
                print("Bravo vous avez gagné en {} tours !".format(self.guesses))
                return
        print("Vous avez perdu... La solution était {} !".format(self.solution))

if __name__ == "__main__":
    mastermind = Mastermind()
    mastermind.play()