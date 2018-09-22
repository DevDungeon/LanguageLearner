import os
import random
import pkg_resources


def print_separator():
    print("=======================")


class LangLearner:

    def __init__(self):
        # Load vocab file options
        self.vocab_filepaths = []
        self.current_vocab_file = None
        self.vocabulary = {}
        vocab_files = pkg_resources.resource_listdir('langlearn', 'vocabulary')
        for f in vocab_files:
            full_path = pkg_resources.resource_filename('langlearn', os.path.join('vocabulary', f))
            self.vocab_filepaths.append(full_path)

    def present_menu(self):
        # List vocab file options
        print_separator()
        for index, filepath in enumerate(self.vocab_filepaths):
            with open(filepath, "rb") as f:
                first_line = f.readline()
                print("%d) %s" % (index+1, first_line.decode('utf8').strip()))
        print_separator()
        choice = input("Enter the number of the vocabulary list you want to practice: ")
        self.current_vocab_file = self.vocab_filepaths[int(choice) - 1]
        print_separator()

    def load_vocab_file(self):
        with open(self.current_vocab_file, "rb") as f:
            title = f.readline()
            print("You chose: %s" % title.decode('utf8').strip())
            print_separator()
            # Load the rest of the lines with the words and translations
            for l in f.readlines():
                line = l.strip()
                split_line = line.split(b'|')
                word = split_line[0].decode('utf8')
                translation = split_line[1].decode('utf8')
                self.vocabulary[word] = translation

    def play_game(self):
        while True:
            random_word = random.choice(list(self.vocabulary.keys()))
            while True:
                print(random_word)
                user_answer = input("Type the word: ")
                if user_answer == random_word:
                    break
                print("Incorrect. Try again.")
            print("Correct. Translation: %s" % self.vocabulary[random_word])
            print_separator()

    def run(self):
        self.present_menu()
        self.load_vocab_file()
        self.play_game()


if __name__ == '__main__':
    langlearner = LangLearner()
    langlearner.run()


