import redis 
from app.config import Config

redis_client = redis.Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)

def cache_get(key):
    return redis_client.get(key)

def cache_set(key, value, ttl=300):
    redis_client.set(key, value, ex=ttl)