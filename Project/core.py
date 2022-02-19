import requests
import itertools
import re
import csv


from collections import OrderedDict 


import util as core_utils

def get_words(min_length=5,max_length=5,capitalization='lower',use_file=''):
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
        with open(f'Docs/{max_length}Words.csv', newline='') as f:
            for row in csv.reader(f):
                WordList.append(row[0])
    else:
        InitialList = requests.get("https://content.instructables.com/ORIG/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt").text
        InitialList = str.splitlines(InitialList)
        for word in InitialList:
            if len(word) >= min_length and len(word) <= max_length:
                WordList.append(word.lower())
    return WordList

def split(word):
    return [char for char in word]


def get_inputs():
    # Enter ??X?? for right letter positions
    
    guess_list = []
    included = str(input("Enter included letters (yellow or green): ")).lower()
    excluded = str(input("Enter excluded letters (grey): ")).lower()

    while True:
        corr_pos = str(input("Enter letters that were in correct positions. The format should be ??a?? where 'a' was a correct letter: ")).lower()
        if len(corr_pos) == 5: break
    
    #remove anything that WAS included
    excluded = ''.join([x for x in excluded if x not in included])
    
    return (included,excluded,corr_pos)


def filter_exclude_possibilities(exclude,word_list):
    return [ele for ele in word_list if all(ch not in ele for ch in split(exclude))]

def filter_include_possibilities(include,word_list):
    return [ele for ele in word_list if any(ch  in ele for ch in split(include))]


def position_check(guess,li):
    expr = guess.replace('?',f'.')
    rx = re.compile(expr)    
    return list(filter(rx.match,li))


def main():
    word_list = get_words()
    good,bad,correct = get_inputs()
    filt_list = filter_include_possibilities(good,word_list)    
    filt_list = filter_exclude_possibilities(bad,filt_list)
    #filter for correct pos
    filt_list = position_check(correct,filt_list)
    #summary on how many char examples there are?
    
    #print(good,bad,correct)
    print(filt_list)
    
if __name__ == '__main__':
    """[summary]
    """
    main()
