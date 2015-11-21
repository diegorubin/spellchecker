# coding: utf-8

import unittest

try:
    from spellchecker.word_list import Word
    from spellchecker import word_list
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    sys.path.append(parentpath)
    from spellchecker.word_list import Word
    from spellchecker import word_list

class TestWord(unittest.TestCase):
    def test_save_word(self):
        word = Word('cachorro', 'SYSTEM-TEST')
        self.assertEqual(True, word.save())

    def test_load_list(self):
        words = word_list.load_list()
        self.assertEqual(True, 'cachorro' in words)

unittest.main()

