# coding: utf-8

import re, collections
import sys
from os.path import join, abspath, dirname


class Spellchecker():
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    def __init__(self, dictionary_file):
        words = self.__get_words(dictionary_file)
        self.NWORDS = self.__train(words)

    def candidates(self, word):
        candidates = self.__known([word]) or self.__known(self.__edits1(word)) or self.__known_edits2(word) or [word]
        return candidates

    def correct(self, word):
        candidates = self.candidates(word)
        return max(candidates, key=self.NWORDS.get)

    def __train(self, features):
        model = collections.defaultdict(lambda: 1)
        for f in features:
            model[f] += 1
        return model

    def __edits1(self, word):
       splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
       deletes    = [a + b[1:] for a, b in splits if b]
       transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
       replaces   = [a + c + b[1:] for a, b in splits for c in self.ALPHABET if b]
       inserts    = [a + c + b     for a, b in splits for c in self.ALPHABET]
       return set(deletes + transposes + replaces + inserts)

    def __known_edits2(self, word):
        return set(e2 for e1 in __edits1(word) for e2 in __edits1(e1) if e2 in self.NWORDS)

    def __known(self, words):
        return set(w for w in words if w in self.NWORDS)

    def __get_words(self, dictionary_file):
        f = abspath(join(dirname(__file__), 'words', dictionary_file))
        words = file(f).read()
        return re.findall('[\w\-]+', words)

