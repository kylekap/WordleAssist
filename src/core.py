import csv
import re
from pathlib import Path

import requests


class Wordle:
    def __init__(self, word_length=5, local_file=""):
        self.word_length = word_length
        self.word_list = self.get_words(use_file=local_file)
        self.remain_words = self.word_list

        self.include, self.exclude, self.correct = self.get_inputs()
        self.remain_words = self.filter_possibilities()

    def get_words(self,*,use_local=""):
        """Get a list of English words from instructables of a desired length.

        Args:
            use_local (string, optional): Alternatively, use a local copy for faster reference

        Returns:
            List: returns a lower case list of words meeting length requirements.

        """
        word_list = []

        if use_local != "":
            with Path(use_local).open(newline="") as f:
                word_list.extend([row[0] for row in csv.reader(f)])
                word_list.extend([row[0] for row in csv.reader(f)])

        else:
            initial_list = requests.get("https://content.instructables.com/ORIG/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt").text  # noqa: S113
            initial_list = str.splitlines(initial_list)
            word_list.extend([word.lower() for word in initial_list if len(word) == self.word_length])
        return word_list

    def split_word(self, word):
            return list(word)

    def get_inputs(self):
        included = str(input("Enter included letters (yellow or green): ")).lower()
        excluded = str(input("Enter excluded letters (grey): ")).lower()

        while True:
            corr_pos = str(input("Enter letters that were in correct positions. The format should be ??a?? where 'a' was a GREEN/CORRECT letter: ")).lower()
            if len(corr_pos) == self.word_length:
                break

        #remove anything that WAS included... just in case
        excluded_letters = "".join([x for x in excluded if x not in included])
        included_letters = set(list(included) + [c for c in corr_pos if c != "?"])

        return (included_letters, excluded_letters, corr_pos)


    def filter_possibilities(self):
        li = [ele for ele in self.remain_words if all(ch not in ele for ch in self.split(self.exclude))] #Excluded
        li = [ele for ele in li if all(ch in ele for ch in self.split(self.include))] #Included
        return self.position_check(li)

    def position_check(self,li):
        expr = self.correct.replace("?",".")
        rx = re.compile(expr)
        return list(filter(rx.match,li))

    def show_remaining(self):
        print(self.remain_words)


def main():
    answer = Wordle(word_len=5, local_file="5letterwords.txt")
    answer.filter_possibilities()
    answer.show_remaining()


if __name__ == "__main__":
    """[summary]
    """
    main()
