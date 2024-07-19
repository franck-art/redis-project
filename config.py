import os

class Config(object):
    CACHE_REDIS_HOST = os.environ['CACHE_REDIS_HOST']
    CACHE_REDIS_PORT = os.environ['CACHE_REDIS_PORT']
    CACHE_REDIS_DB = os.environ['CACHE_REDIS_DB']
    CACHE_REDIS_PASSWORD = os.environ['CACHE_REDIS_PASSWORD']
    CACHE_TYPE = 'redis'