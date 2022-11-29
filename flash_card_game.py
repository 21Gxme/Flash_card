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
        print("*-" * 20 + "*")
        print("Welcome to Flash Card Game")
        print("Press select mode to start the game")
        try:
            choice = int(input("Flash Card Game from CSV file Press(1): \n"
                               "Flash Card Game from users Press(2): \n"))
            print("*-" * 20 + "*")
            if choice == 1:
                press = input('Press (R)ead or (W)rite: ')
                if press == 'R' or press == 'r':
                    self.word = read_write().read()
                    self.display()
                elif press == 'W' or press == 'w':
                    self.word = read_write().write()
                    self.display()
                else:
                    print("Invalid input")
                    self.start()
            elif choice == 2:
                self.word = Get_Vocab().get_vocabulary()
                self.display()
        except ValueError:
            print("Invalid input")
            self.start()

    def display(self):
        print("Press Q to exit")
        while True:
            try:
                if len(self.word) <= 0:
                    print("You have completed all the words")
                    exit()
            except TypeError:
                print("something went wrong")
                print('-' * 25)
                self.start()
            print(f'HP: {self.hp}')
            vocab = random.choice(list(self.word.keys()))
            vocab_dict = self.word.pop(vocab)
            print('=' * 20)
            print(f'{vocab:^20}')
            print('=' * 20)
            meaning = input("Enter the answer: ")
            if vocab_dict == meaning:
                print("Correct")
                if self.hp < 3:
                    self.hp += 1
            elif meaning == 'Q' or meaning == 'q':
                print('♡' * 20)
                break
            elif vocab_dict != meaning:
                print("Incorrect")
                self.word[vocab] = vocab_dict
                self.__hp -= 1
                if self.hp > 0:
                    print(f"You have {self.__hp} lives left")
                elif self.__hp <= 0:
                    show = f"You have {self.__hp} lives left"
                    print(f"{show:^47}")
                    print(f"{'Game Over':^47}")
                    print('(T⌓T) (┳Д┳) (ಥ﹏ಥ) ( ╥ω╥ ) (⋟﹏⋞) (;﹏;) (ㄒoㄒ) ಥ_ಥ')
                    exit()
            else:
                print("Invalid input")
                self.display()


if __name__ == '__main__':
    FlashCardGame().start()
