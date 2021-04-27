import aiohttp
import asyncio
import random

from datetime import datetime
from lib.utils import get_stream, get_client
from lib.streams.movies import USERNAME, PROJECT, STREAM


async def write_data():
    # First, get and start the client
    client = await get_client()
    await client.start()

    # Write a whole dataset as an example
    # load a dataset of movies
    url = "https://raw.githubusercontent.com/vega/vega/master/docs/data/movies.json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            movies = await res.json(content_type=None)

    # Get the stream
    stream = await get_stream(USERNAME, PROJECT, STREAM)

    # write a 100 random movies one-by-one
    n = 10
    for i in range(n):
        # get a random movie
        movie = random.choice(movies)

        # transform and write the movie
        await stream.write({
            "title": str(movie["Title"]),
            "released_on": datetime.strptime(movie["Release Date"], "%b %d %Y"),
            "director": movie["Director"],
            "budget_usd": movie["Production Budget"],
            "rating": movie["IMDB Rating"],
        })

        # wait a while
        await asyncio.sleep(1)

    await client.stop()
