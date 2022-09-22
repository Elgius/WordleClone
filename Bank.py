import random

WOTD = []

data = open("data.txt", "r")

reader = data.read()


WOTD = reader.split("\n")

data.close()

Key = random.choice(WOTD)


print(WOTD)

print(Key)