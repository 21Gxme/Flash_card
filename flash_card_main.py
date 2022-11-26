
from flash_card_game import FlashCardGame
from show_flash_card import show_flash_card


class flash_card:
    def __init__(self, vocabulary, meaning):
        self.vocabulary = vocabulary
        self.meaning = meaning
        self.word = {}

    def start(self, vocabulary, meaning):
        print("Welcome to Flash Card Game")
        print("Press select mode to start the game")
        try:
            choice = int(input("Flash Card Game press 1: \n"
                               "Show Flash Card press 2: \n"))
            if choice == 1:
                FlashCardGame(vocabulary, meaning).start()
            elif choice == 2:
                show_flash_card(vocabulary, meaning).start()
            elif choice == 3:
                print("Thank you for playing")
                exit()
            else:
                print("Invalid input")
                self.start(vocabulary, meaning)
        except ValueError:
            print("Invalid input")
            self.start(vocabulary, meaning)


flash_card('start','start')
