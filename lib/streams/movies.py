import beneath
import os

from dotenv import load_dotenv
from lib.utils import get_client


USERNAME = 'sarahmk125'
PROJECT = 'demo'
STREAM = 'movies'


def create_stream():
    client = get_client()
    await client.start()

    stream = await client.create_stream(
        f"{USERNAME}/{PROJECT}/{STREAM}",
        schema="""
            " A stream of movies "
            type Movie @schema {
                title: String! @key
                released_on: Timestamp! @key
                director: String
                budget_usd: Int
                rating: Float
            }
        """,
        update_if_exists=True)
