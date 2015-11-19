# coding: utf-8

import redis, ConfigParser
import os.path

class RedisConnection():
    def __init__(self):
        self.load_configurations()

    def __load_configurations(self):
        self.config = ConfigParser.ConfigParser()
        if os.path.exists('~/.spellchecker-server.cfg'):
            config.read('~/.spellchecker-server.cfg')
        else:
            config.read('/etc/spellchecker/server.cfg')

        self.redis_host = config.get('redis', 'host')
        self.redis_port = config.get('redis', 'port')

class WordList():
    def __init__(self):
        pass

class Word():
    def __init__(self, word, author):
        self.word = word
        self.author = author

    def save(self):
        self.lpush('words', word)
        self.lpush('author:%s'%(author), word)


