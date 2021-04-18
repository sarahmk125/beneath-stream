import asyncio

from lib.data.movies import write_data
from lib.streams.movies import create_stream


async def runner():
    await create_stream()
    await write_data()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(runner())
