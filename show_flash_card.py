import random
from Read_write import read_write
from Get_Vocab import Get_Vocab


class show_flash_card:
    def __init__(self):
        self.word = {}

    def start(self):
        print("*-" * 20 + "*")
        print("Welcome to Show Flash Card")
        print("Press select mode to start the game")
        try:
            print('Show Flash Card from CSV file Press(1)\n'
                  'Show Flash Card from users Press(2)')
            print("*-" * 20 + "*")
            choice = int(input('Enter your choice: '))
            if choice == 1:
                press = input('Press (R)ead or (W)rite: ')
                if press == 'R' or press == 'r':
                    self.word = read_write().read()
                    self.display()
                elif press == 'W' or press == 'w':
                    self.word = read_write().write()
                    self.display()
                elif press == 'Q' or press == 'q':
                    self.start()
                else:
                    print("Invalid input")
                    self.start()
            elif choice == 2:
                self.word = Get_Vocab().get_vocabulary()
                self.display()
            else:
                print("Invalid input")
                self.start()
        except ValueError:
            print("Invalid input")
            self.start()

    def display(self):
        print("Press Q to exit")
        try:
            while True:
                try:
                    if len(self.word) == 0:
                        print("You have completed all the words")
                        print('♡'*41)
                        exit()
                except TypeError:
                    print("something went wrong")
                    print('-' * 41)
                    self.start()
                vocab = random.choice(list(self.word.keys()))
                print(f'=' * 41)
                print(f'{vocab:^41}')
                print('=' * 41)
                press = input("Press (M)eaning or (N)ext: ")
                if press == 'M' or press == 'm':
                    print('-' * 41)
                    print(f"{self.word[vocab]:^41}")
                    print('-' * 41)
                    press = input("Press (N)ext or (Q)uit: ")
                    while True:
                        if press == 'N' or press == 'n':
                            break
                        elif press == 'Q' or press == 'q':
                            exit()
                            print("Thank you for playing")
                            print('♡' * 41)
                        else:
                            print("Invalid input")
                            press = input("Press (N)ext or (Q)uit: ")
                elif press == 'Q' or press == 'q':
                    print("Thank you for playing")
                    print('♡'*41)
                    break
                elif press == 'N' or press == 'n':
                    del self.word[vocab]
                    continue
                else:
                    print('-' * 41)
                    print(f"{'Invalid input':^41}")
                    print('-' * 41)
        except ValueError:
            print('-' * 41)
            print(f"{'Invalid input':^41}")
            print('-' * 41)
            self.display()


if __name__ == '__main__':
    show_flash_card().start()
