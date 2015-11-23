# coding: utf-8

import cyclone.web
import re
from spellchecker import Spellchecker
from word_list import Word

spellchecker = Spellchecker('words')

class CheckWordHandler(cyclone.web.RequestHandler):
    def get(self, word):
        self.set_header("Content-Type", "application/json")
        self.write(spellchecker.verify_and_analyze(word))

class CheckTextHandler(cyclone.web.RequestHandler):
    def post(self):
        text = self.request.body.decode('utf-8')
        self.set_header("Content-Type", "application/json")
        self.write(spellchecker.verify_and_analyze_text(text))

class WordListHandler(cyclone.web.RequestHandler):
    def post(self):
        self.set_header("Content-Type", "application/json")

        word = self.get_argument('word')
        author = self.get_argument('author')

        w = Word(word, author)
        if w.save():
            spellchecker.add(word)

        self.write({'word': word, 'author': author})

class ApplicationServer(cyclone.web.Application):
    def __init__(self):
        handlers = [
            (r"/check/(.{1,50})", CheckWordHandler),
            (r"/check_text", CheckTextHandler),
            (r"/add", WordListHandler)
        ]

        settings = {}

        cyclone.web.Application.__init__(self, handlers, **settings)

