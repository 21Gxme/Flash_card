from show_flash_card import show_flash_card

class Get_Vocab:
    def __init__(self, file_name):
        self.file_name = file_name
        self.word = {}
        self.get_vocab()

    def get_vocab(self):
        print("Enter the vocabulary and meaning (Press Q to exit)")
        while True:
            vocab = input("Enter the vocabulary: ")
            if vocab == "Q" or vocab == 'q':
                continue
            else:
                meaning = input("Enter the meaning: ")
                self.word[vocab] = meaning
        return self.word