# coding: utf-8

import redis
import os

class RedisConnection():
    def __init__(self):
        self.__load_configurations()

    def __load_configurations(self):

        if hasattr(RedisConnection, 'connection'):
            self.connection = RedisConnection.connection
        else:
            print 'creating a new connection with redis'
            self.redis_host = os.environ.get('SPELLCHECKER_REDIS_HOST', 'localhost')
            self.redis_port = os.environ.get('SPELLCHECKER_REDIS_PORT', '6379')

            self.connection = redis.StrictRedis(host=self.redis_host, port=self.redis_port, db=0)
            RedisConnection.connection = self.connection

    def add_to_list(self, listname, content):
        self.connection.lpush(listname,content)

    def load_list(self, listname):
        return self.connection.lrange('words', 0, -1)

class Word():
    def __init__(self, word, author):
        self.word = word
        self.author = author
        self.connection = RedisConnection()

    def save(self):
        print 'adding %s for %s'%(self.word, self.author)
        self.connection.add_to_list('words', self.word)
        self.connection.add_to_list('author:%s'%(self.author), self.word)
        return True

def load_list():
    connection = RedisConnection()
    return connection.load_list('words')


