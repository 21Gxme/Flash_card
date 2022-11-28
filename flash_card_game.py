import random
from Read_write import read_write
from Get_Vocab import Get_Vocab


class FlashCardGame:
    def __init__(self):
        self.word = {}
        self.__hp = 3

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    def start(self):
        print("Welcome to Flash Card Game")
        print("Press select mode to start the game")
        try:
            choice = int(input("Flash Card Game from CSV file Press(1): \n"
                               "Flash Card Game from users Press(2): \n"))
            if choice == 1:
                press = input('Press (R)ead or (W)rite: ')
                if press == 'R' or press == 'r':
                    self.word = read_write().read()
                    self.display()
                elif press == 'W' or press == 'w':
                    self.word = read_write().write()
                    self.display()
            elif choice == 2:
                self.word = Get_Vocab().get_vocabulary()
                self.display()
        except ValueError:
            print("Invalid input")
            self.start()

    def display(self):
        print("Press Q to exit")
        while True:
            if len(self.word) == 0:
                print("You have completed all the words")
                exit()
            vocab = random.choice(list(self.word.keys()))
            vocab_dict = self.word.pop(vocab)
            print(f'='*20)
            print(f'{vocab:^20}')
            print('='*20)
            meaning = input("Enter the meaning: ")
            if vocab_dict == meaning:
                print("Correct")
                self.hp += 1
                print(f"Your HP is {self.__hp}")
            elif meaning == 'Q' or meaning == 'q':
                break
            elif vocab_dict != meaning:
                print("Incorrect")
                self.__hp -= 1
                print(f"You have {self.__hp} lives left")
                if self.__hp == 0:
                    print("Game Over")
                    exit()
            else:
                print("Invalid input")
                self.display()


if __name__ == '__main__':
    FlashCardGame().start()