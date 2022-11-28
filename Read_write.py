import csv


class read_write:

    def write(self):
        with open(input("Enter the file name: "), 'a', newline='') as file:
            while True:
                vocab = input("Enter the vocabulary: ")
                if vocab == "Q" or vocab == 'q':
                    break
                else:
                    meaning = input("Enter the meaning: ")
                    writer = csv.writer(file)
                    writer.writerow([vocab, meaning])
        return self.read()

    def read(self):
        with open(input("Enter the file name: "), 'r') as file:
            reader = csv.reader(file)
            return dict(reader)

if __name__ == '__main__':
    # read_write().write()
    print(read_write().read())

