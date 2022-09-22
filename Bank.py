import random



class bank:
    def stuff(self):
        WOTD = []

        data = open("data.txt", "r")

        reader = data.read()


        WOTD = reader.split("\n")

        data.close()

        Key = random.choice(WOTD)

        self.key = Key

        return Key

word = bank()

print(word)