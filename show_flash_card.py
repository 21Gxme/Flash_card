import random
from Read_write import read_write
from Get_Vocab import Get_Vocab


class show_flash_card:
    def __init__(self, vocabulary, meaning):
        self.vocabulary = vocabulary
        self.meaning = meaning
        self.word = {}
        self.start(vocabulary, meaning)

    def start(self, vocabulary, meaning):
        print("Welcome to Show Flash Card")
        print("Press select mode to start the game")
        try:
            choice = int(input("Show Flash Card from CSV file Press(1): \n"
                               "Show Flash Card from users Press(2): \n"))
            if choice == 1:
                read_write(self)
            elif choice == 2:
                Get_Vocab(self)
        except ValueError:
            print("Invalid input")
            self.start(vocabulary, meaning)

    def display(self):
        print("Press Q to exit")
        while True:
            vocab = random.choice(self.vocabulary)
            meaning = self.word[vocab]
            print("Vocabulary: ", vocab)
            user_input = input("Press Enter to see the next word or (S)how the word: ")
            if user_input == "S" or user_input == "s":
                print("Meaning: ", meaning)
                self.word[vocab] = meaning
            if user_input == "Q" or user_input == 'q':
                break