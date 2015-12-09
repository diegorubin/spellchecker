# coding: utf-8

import unittest

try:
    from spellchecker.spellchecker import Spellchecker
    from spellchecker.word_list import Word
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    sys.path.append(parentpath)
    from spellchecker.word_list import Word
    from spellchecker.spellchecker import Spellchecker


class TestSpellchecker(unittest.TestCase):
    def setUp(self):
        self.spellchecker = Spellchecker('pt_BR.list')
        word = Word('abacaxi', 'TEST')

    def test_correct(self):
        self.assertEqual('abacaxi', self.spellchecker.correct('abacahi'))

    def test_if_correct(self):
        self.assertEqual('abacaxi', self.spellchecker.correct('abacaxi'))

    def test_candidates(self):
        self.assertEqual(set(['abacaxi']), self.spellchecker.candidates('abacahi'))


