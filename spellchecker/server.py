# coding: utf-8

import cyclone.web

class CheckWordHandler(cyclone.web.RequestHandler):
    def get(self, word):
        self.set_header("Content-Type", "application/json")

        response = {
            'status' : 200,
            'word' : word
        }

        self.write(response)

class ApplicationServer(cyclone.web.Application):
    def __init__(self):
        handlers = [
            (r"/check/([\w\-]+)", CheckWordHandler)
        ]

        settings = {}

        cyclone.web.Application.__init__(self, handlers, **settings)

