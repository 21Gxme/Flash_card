import csv


class read_write:

    def write(self):
        try:
            with open(input("Enter the file name: "), 'a', newline='') as file:
                while True:
                    vocab = input("Enter the vocabulary: ")
                    if vocab == "Q" or vocab == 'q':
                        break
                    else:
                        meaning = input("Enter the meaning: ")
                        writer = csv.writer(file)
                        writer.writerow([vocab, meaning])
        except FileNotFoundError:
            print("File not found")
            self.write()
        return self.read()

    def read(self):
        try:
            with open(input("Enter the file name: "), 'r') as file:
                reader = csv.reader(file)
                return dict(reader)
        except FileNotFoundError:
            print("File not found")
            self.read()


if __name__ == '__main__':
    # read_write().write()
    print(read_write().read())

