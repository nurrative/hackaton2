import redis
from kombu.transport.redis import PrefixedStrictRedis

redis_client = redis.Redis(host='localhost', port=6379, db=0)
prefixed_redis_client = PrefixedStrictRedis('prefix', redis_client)

