import requests
import re
import csv

import pandas as pd

import util as core_utils


class Wordle:
    def __init__(self, word_len,use=''):
        self.word_length = word_len
        self.word_list = self.get_words(capitalization='lower',use_file=use)
        self.remain_words = self.word_list
        self.include, self.exclude, self.correct = self.get_inputs()
        self.remain_words = self.filter_possibilities()
        return None

    def get_words(self,capitalization='lower',use_file=''):
        """Gets a list of english words from instructables of a desired length.

        Args:
            min_length (int, optional): Keep words of this length or longer. Defaults to 5.
            min_length (int, optional): Keep words of this length or shorter. Defaults to 5.
            capitalizaton (string, optional): Capitalization rules of the word list to return (lower, upper, title). Defaults to lower.
            use_local (boolean, optional): Alternatively, use a local copy for faster reference

        Returns:
            List: returns a lower case list of words meeting length requirements.
        """
        WordList = []

        if len(use_file) > 0:
            with open(f'Docs/{self.word_length}Words.csv', newline='') as f:
                for row in csv.reader(f):
                    WordList.append(row[0])
        else:
            InitialList = requests.get("https://content.instructables.com/ORIG/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt").text
            InitialList = str.splitlines(InitialList)
            for word in InitialList:
                if len(word) == self.word_length:
                    WordList.append(word.lower())
        return WordList

    def split(self, word):
        return [char for char in word]

    def get_inputs(self):
        guess_list = []
        included = str(input("Enter included letters (yellow or green): ")).lower()
        excluded = str(input("Enter excluded letters (grey): ")).lower()

        while True:
            corr_pos = str(input("Enter letters that were in correct positions. The format should be ??a?? where 'a' was a correct letter: ")).lower()
            if len(corr_pos) == self.word_length: break
    
        #remove anything that WAS included... just in case
        excluded = ''.join([x for x in excluded if x not in included])
    
        return (included,excluded,corr_pos)


    def filter_possibilities(self):
        li = [ele for ele in self.remain_words if all(ch not in ele for ch in self.split(self.exclude))] #Excluded
        li = [ele for ele in li if all(ch in ele for ch in self.split(self.include))] #Included
        li = self.position_check(li) #Exact placements
        return li


    def position_check(self,li):
        expr = self.correct.replace('?',f'.')
        rx = re.compile(expr)    
        return list(filter(rx.match,li))

    def show_remaining(self):
        print(self.remain_words)


def main():
    answer = Wordle(word_len=5)
    answer.filter_possibilities()
    answer.show_remaining()
    return None

    
if __name__ == '__main__':
    """[summary]
    """
    main()
