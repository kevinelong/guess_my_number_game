import random


class Game(object):
    def __init__(self, limit=10):
        self.limit = limit
        self.text = None
        self.playing = True
        self.picked = None
        self.is_match = None
        self.reset()

    def reset(self):
        self.picked = str(random.randint(1, self.limit))
        self.is_match = False

    def guess(self):
        guess = input("Guess")

        if guess == "":
            self.playing = False
            return

        is_match = (guess == self.picked)

        if is_match:
            print("\nCorrect! the number was: " + self.picked)
            self.is_match = False
            self.reset()
            self.show_rules()
            return

        if guess.isnumeric():
            result = "HIGH" if int(guess) > int(self.picked) else "LOW"
            print("Your guess (" + guess + ") is too " + result + "!")

    @staticmethod
    def show_rules():
        print("\nI am thinking of a number between 1 and 10. Enter your guess or blank line to quit.")

    def play(self):
        while self.playing:
            while self.playing and not self.is_match:
                self.guess()
        print("\nGoodbye!")


game = Game()
game.play()
