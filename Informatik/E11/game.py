import os
import random
from difflib import SequenceMatcher
from abc import ABC, abstractmethod


class GameLogic(ABC):

    @abstractmethod
    def __init__(self, num_words, length, attempts):
        pass

    @abstractmethod
    def word_selection(self):
        pass

    @abstractmethod
    def check(self):
        pass


class NumberLogic(GameLogic):

    def __init__(self, num_words, length, attempts):
        self.num_words = num_words
        self.length = length
        self.attempts = attempts
        self.words = self.word_selection()
        self.password = random.choice(self.words)

    def word_selection(self):
        numbers = []
        for i in range(self.num_words):
            numbers.append(str(self.random_n_digit_number(self.length)))

        return numbers

    def check(self, guess):

        if len(guess) != len(self.password):
            return False, ["Wrong length"]
        if guess == self.password:
            return True, ["Access granted!"]
        else:
            matching_digits = 0
            for digit in guess:
                if digit in self.password:
                    matching_digits += 1
            return False, ["{}/{} correct".format(matching_digits, len(self.password))]


    def random_n_digit_number(self, n):
        range_start = 10**(n-1)
        range_end = 10**n - 1
        return random.randint(range_start, range_end)


class WordLogic(GameLogic):
    """Internal game logic"""

    def __init__(self, num_words, length, attempts):
        """Set up a new game with the provided parameters"""
        self.num_words = num_words
        self.length = length
        self.attempts = attempts
        self.words = self.word_selection()
        self.password = random.choice(self.words)

    def word_selection(self):
        with open("words.txt") as f:
            word_list = f.read().splitlines()

        fixed_length_words = [word.upper() for word in word_list if len(word) is self.length]

        random.shuffle(fixed_length_words)
        selected_words = []
        for i in range(round(self.num_words/3)):
            selected_words.append(fixed_length_words[i])

        while len(selected_words) < self.num_words:
            random_word_from_selected = random.choice(selected_words)
            random_word_from_pool = random.choice(fixed_length_words)
            if self.compute_similarity(random_word_from_pool, random_word_from_selected, 0.6):
                selected_words.append(random_word_from_pool)

        return selected_words

    def compute_similarity(self, a, b, threshold):
        return threshold > SequenceMatcher(None, a, b).ratio()

    def check(self, guess):
        """Check a guess and give feedback"""
        if len(guess) != self.length:
            return False, ["Wrong length"]
        if guess == self.password:
            return True, ["Access granted!"]
        else:
            matching = 0
            for i in range(self.length):
                if guess[i] == self.password[i]: matching += 1
            self.attempts = self.attempts - 1
            return False, ["%d/%d correct" % (matching, self.length), "Access denied!"]


class GameRunner(object):
    """Interactive game front-end"""

    def __init__(self, logic):
        """Interact with the given game logic"""
        self.logic = logic
        self.rows = 17
        self.columns = 2
        self.colwidth = 12
        self.code_snippet = self.generate_code_lines()
        self.hex_codes = self.generate_hex_codes()

    def generate_hex_codes(self):
        hex_code = []
        for i in range(self.columns * self.rows):
            sequence = "0x"
            hex_digits = "0123456789ABCDEF"
            for j in range(4):
                sequence = sequence + random.choice(hex_digits)
            hex_code.append(sequence)

        return hex_code

    def generate_code_lines(self):
        padding_chars = "<>[]{}()'|\"!@#$%^&*-_+=.;:?,/"
        len_snippet = self.rows * self.columns * self.colwidth
        len_words = self.logic.num_words * self.logic.length
        len_paddings = len_snippet - len_words
        padding_size = int(len_paddings / (self.logic.num_words + 1))

        def generate_padding():
            return "".join([random.choice(padding_chars) for i in range(padding_size)])

        text = ""
        text += generate_padding()
        for word in self.logic.words:
            text += "".join([c for c in word])
            text += generate_padding()
        text += generate_padding()
        text = text[:len_snippet]
        return [text[i:i + self.colwidth] for i in range(0, len(text), self.colwidth)]

    def print_screen(self, history):
        """Redraw the entire terminal screen with the given content"""
        # Clear the terminal screen
        print()
        os.system('cls' if os.name == 'nt' else 'clear')
        # Print screen contents
        print("ROBCO INDUSTRIES (TM) TERMALINK PROTOCOL\n" + \
              "ENTER PASSWORD NOW\n\n" + \
              str(self.logic.attempts) + " ATTEMPT(S) LEFT:" + (" █" * self.logic.attempts) + "\n")
        local_history = history[-self.rows + 1:]
        history_lines = ["" for i in range(self.rows - len(local_history) - 1)] + \
                        [">%s" % l for l in local_history] + [">"]
        for row in range(self.rows):
            # print address and text cells
            for column in range(self.columns):
                offset = self.rows * column
                index = offset + row
                print("%s %s  " % (self.hex_codes[index], self.code_snippet[index]), end="")
            print(history_lines[row], end="")
            if not row == self.rows - 1:
                print()

    def run(self):
        """Run the game main loop"""

        history = []

        self.print_screen(history)
        while self.logic.attempts != 0:
            guess = input().upper()
            history.append(guess)
            access, feedback = logic.check(guess)
            history.extend(feedback)
            self.print_screen(history)
            if access:
                break


if __name__ == '__main__':
    logic = NumberLogic(num_words=7, length=4, attempts=4)
    runner = GameRunner(logic)
    runner.run()
