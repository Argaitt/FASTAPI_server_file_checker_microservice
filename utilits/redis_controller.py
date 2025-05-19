import asyncio
from redis.asyncio import Redis

async def redis_init():
    redis = Redis(
        host='localhost',
        port=6379,
        password=None,
        decode_responses=True
    )

    await redis.ping()
    print("redis connect successful")
    return redis

