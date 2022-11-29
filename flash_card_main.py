from flash_card_game import FlashCardGame
from show_flash_card import show_flash_card


class flash_card:
    def start(self):
        print("Welcome to Flash Card")
        print("Press select mode to start the game")
        try:
            choice = int(input("Flash Card Game press 1: \n"
                               "Show Flash Card press 2: \n"
                               "Exit press 3: \n"))
            if choice == 1:
                FlashCardGame().start()
            elif choice == 2:
                show_flash_card().start()
            elif choice == 3:
                print("Thank you for playing")
                exit()
            else:
                print("Invalid input")
                print('-' * 25)
                self.start()
        except ValueError:
            print("Invalid input")
            print('-' * 25)
            self.start()


if __name__ == '__main__':
    flash_card().start()
