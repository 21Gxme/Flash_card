import os
from flash_card_game import FlashCardGame
from show_flash_card import show_flash_card


class flash_card:
    def start(self):
        print("""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▀▀ █░░ ▄▀█ █▀ █░█   █▀▀ ▄▀█ █▀█ █▀▄
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █▀░ █▄▄ █▀█ ▄█ █▀█   █▄▄ █▀█ █▀▄ █▄▀
""")
        print("*+" * 20 + "*")
        print("Press select mode to start the game")
        try:
            print("Flash Card Game press (1) \n"
                  "Show Flash Card press (2) \n"
                  "Exit press (3): ")
            print("*+" * 20 + "*")
            choice = int(input('Enter your choice: '))
            if choice == 1:
                os.system('clear')
                FlashCardGame().start()
            elif choice == 2:
                os.system('clear')
                show_flash_card().start()
            elif choice == 3:
                print("Thank you for playing")
                exit()
            else:
                print('-' * 40)
                print(f"{'Invalid input':^40}")
                print('-' * 40)
                self.start()
        except ValueError:
            print('-' * 40)
            print(f"{'Invalid input':^40}")
            print('-' * 40)
            self.start()


if __name__ == '__main__':
    flash_card().start()
