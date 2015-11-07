# coding: utf-8

import cyclone.web
from spellchecker import Spellchecker

spellchecker = Spellchecker('pt_BR.wl')

class CheckWordHandler(cyclone.web.RequestHandler):
    def get(self, word):
        self.set_header("Content-Type", "application/json")

        correct = spellchecker.correct(word)
        candidates = spellchecker.candidates(word)

        response = {
            'status' : 200,
            'word' : word,
            'suggestion': correct,
            'wrong' : correct != word,
            'candidates' : list(candidates)
        }

        self.write(response)

class ApplicationServer(cyclone.web.Application):
    def __init__(self):
        handlers = [
            (r"/check/([\w\-]+)", CheckWordHandler)
        ]

        settings = {}

        cyclone.web.Application.__init__(self, handlers, **settings)

