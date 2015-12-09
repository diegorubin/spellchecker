# coding: utf-8

import unittest

import sys
from os.path import join, abspath, dirname
parentpath = abspath(join(dirname(__file__), '..'))
sys.path.append(parentpath)
from spellchecker.spellchecker import Spellchecker

from test_spellchecker import TestSpellchecker
from test_word_list import TestWord

unittest.main()

