
class Get_Vocab:
    def __init__(self):
        self.word = {}
        self.get_vocabulary()

    def get_vocabulary(self):
        print("Enter the vocabulary and meaning (Press Q to exit)")
        while True:
            vocab = input("Enter the vocabulary: ")
            if vocab == "Q" or vocab == 'q':
                break
            else:
                meaning = input("Enter the meaning: ")
                self.word[vocab] = meaning
        return self.word


if __name__ == '__main__':
    Get_Vocab().get_vocabulary()