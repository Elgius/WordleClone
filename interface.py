from typing import List
from wordle import Wordle
from letter_state import letterState
import random
#from Bank import Wdata

from colorama import Fore

def main():
    word_set = load_word("data.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)


    while wordle.can_attempt:

        x = input("\nWhat do you think todays word is?:  \n")

        if len(x) != wordle.MAX_ATTEMPTS :
            print(Fore.RED + f"Your entry must be {wordle.MAX_ATTEMPTS} characters" + Fore.RESET)
            continue

        wordle.attempt(x)

        display_word(wordle)

        
        
        if wordle.is_solved:
            print("you have solved the puzzle!")
        else:
            print("\n You have failed to solve the puzzle \n")
        
        if (wordle.remaining_attempts == 0):
            print(f"the word was {secret}")


def display_word(wordle: Wordle):
    print("\n Your results so far \n")
    print(f"\n You have {wordle.remaining_attempts} attempts remaining to solve puzzle! \n")
    for word in wordle.attempts:
        result = wordle.guess(word)
        #css = result_to_colour(result)
        css = convert_result_to_color(result)
        print(css)
    for _ in range(wordle.remaining_attempts):
        print(" ".join(["_"] * wordle.MAX_LENGTH))



def convert_result_to_color(result: List[letterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW

        else:
            color = Fore.WHITE

        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)

    return " ".join(result_with_color)
        

def load_word(path : str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)

        return word_set





if __name__ == "__main__":
    main()
