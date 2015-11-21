# coding: utf-8

import re, collections
import sys
from os.path import join, abspath, dirname

from word_list import load_list

class Spellchecker():
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzãâàáéêíõóôúç'.decode('utf-8')
    def __init__(self, dictionary):
        words = self.__get_words(dictionary)
        self.NWORDS = self.__train(words)

    def candidates(self, word):
        candidates = self.__known([word]) or self.__known(self.__edits1(word)) or self.__known_edits2(word) or [word]
        return candidates

    def correct(self, word):
        candidates = self.candidates(word)
        return max(candidates, key=self.NWORDS.get)

    def verify_and_analyze_text(self, text):
        result = {'original' : text, 'wrongs' : []}
        for number, line in enumerate(text.split("\n")):
            for match in re.finditer('([\w\-_]+)', line, re.UNICODE):
                word = self.verify_and_analyze(match.group(1))
                if word['wrong']:
                    word['line'] = number
                    word['column'] = match.start()
                    result['wrongs'].append(word)

        return result

    def verify_and_analyze(self, word):
        print 'checking word %s'%(word)
        correct = self.correct(word)
        candidates = self.candidates(word)

        response = {
            'word' : word,
            'suggestion': correct,
            'wrong' : correct != word,
            'candidates' : list(candidates)
        }

        return response

    def add(self, word):
        self.NWORDS[unicode(word, 'utf-8')] += 1

    def __train(self, features):
        print 'trainning spellchecker'
        model = collections.defaultdict(lambda: 1)
        for f in features:
            model[unicode(f, 'utf-8')] += 1
        return model

    def __edits1(self, word):
       splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]

       deletes    = [a + b[1:] for a, b in splits if b]
       transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
       replaces   = [a + c + b[1:] for a, b in splits for c in self.ALPHABET if b]
       inserts    = [a + c + b     for a, b in splits for c in self.ALPHABET]
       return set(deletes + transposes + replaces + inserts)

    def __known_edits2(self, word):
        return set(e2 for e1 in self.__edits1(word) for e2 in self.__edits1(e1) if e2 in self.NWORDS)

    def __known(self, words):
        return set(w for w in words if w in self.NWORDS)

    def __get_words(self, dictionary_file):
        return load_list()

