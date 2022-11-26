
from Read_write import read_write
from Get_Vocab import Get_Vocab


class FlashCardGame:
    def __init__(self, vocabulary, meaning):
        self.vocabulary = vocabulary
        self.meaning = meaning
        self.word = {}
        self.start(vocabulary, meaning)

    def start(self, vocabulary, meaning):
        print("Welcome to Flash Card Game")
        print("Press select mode to start the game")
        try:
            choice = int(input("Flash Card Game from CSV file: \n"
                               "Flash Card Game from users: \n"))
            if choice == 1:
                read_write()
            elif choice == 2:
                Get_Vocab()
        except ValueError:
            print("Invalid input")
            self.start(vocabulary, meaning)