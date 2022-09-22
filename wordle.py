from letter_state import letterState

class Wordle:

    MAX_LENGTH = 6
    MAX_ATTEMPTS = 5

    def __init__(self, secret: str):
        self.secret : str = secret.upper()
        self.attempts =[]
        pass

    def attempt(self, word:str):
        word = word.upper()
        self.attempts.append(word)

    def guess(self, word:str):
        word = word.upper()
        results = []

        for i in range(self.MAX_ATTEMPTS):
            character = word[i]
            letter = letterState(character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = character == self.secret[i]
            results.append(letter)

        return results

    @property    
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return len(self.attempts) < self.MAX_ATTEMPTS > 0 and not self.is_solved

    
