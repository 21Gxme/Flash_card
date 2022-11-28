import random
from Read_write import read_write
from Get_Vocab import Get_Vocab


class show_flash_card:
    def __init__(self):
        self.vocabulary = None
        self.meaning = None
        self.word = None

    def start(self):
        print("Welcome to Show Flash Card")
        print("Press select mode to start the game")
        try:
            choice = int(input("Show Flash Card from CSV file Press(1): \n"
                               "Show Flash Card from users Press(2): \n"))
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
        try:
            while True:
                if len(self.word) == 0:
                    print("You have completed all the words")
                    exit()
                vocab = random.choice(list(self.word.keys()))
                print(f'=' * 20)
                print(f'{vocab:^20}')
                print('=' * 20)
                press = input("Press (M)eaning or (N)ext: ")
                if press == 'M' or press == 'm':
                    print('=' * 20)
                    print(f"{self.word[vocab]:^20}")
                    print('=' * 20)
                elif press == 'Q' or press == 'q':
                    break
                elif press == 'N' or press == 'n':
                    _ = self.word.pop(vocab)
                    continue
                else:
                    print("Invalid input")
        except ValueError:
            print("Invalid input")
            self.display()


if __name__ == '__main__':
    show_flash_card().start()
