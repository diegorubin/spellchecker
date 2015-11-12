# coding: utf-8

import cyclone.web
import re
from spellchecker import Spellchecker

spellchecker = Spellchecker('pt_BR.wl')

class CheckWordHandler(cyclone.web.RequestHandler):
    def get(self, word):
        self.set_header("Content-Type", "application/json")
        self.write(spellchecker.verify_and_analyze(word))

class CheckTextHandler(cyclone.web.RequestHandler):
    def post(self):
        text = self.request.body
        self.set_header("Content-Type", "application/json")
        self.write(spellchecker.verify_and_analyze_text(text))

class ApplicationServer(cyclone.web.Application):
    def __init__(self):
        handlers = [
            (r"/check/(.{1,50})", CheckWordHandler),
            (r"/check_text", CheckTextHandler)
        ]

        settings = {}

        cyclone.web.Application.__init__(self, handlers, **settings)

