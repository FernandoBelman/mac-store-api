import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongo:27017/mac_store')
    REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
    REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

        