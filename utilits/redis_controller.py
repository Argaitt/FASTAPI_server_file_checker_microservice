import asyncio
import logging

from redis.asyncio import Redis

logger = logging.getLogger("app")

async def redis_init():
    redis = Redis(
        host='172.16.238.215',
        port=6379,
        password=None,
        decode_responses=True
    )

    await redis.ping()
    logger.info("redis connect successful")
    return redis

