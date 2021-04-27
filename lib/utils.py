import os
import beneath

from dotenv import load_dotenv


USERNAME = 'sarahmk125'
SECRETS_FILE = 'secrets.env'


async def get_client():
    load_dotenv(SECRETS_FILE)
    secret = os.getenv('BENEATH_SECRET')
    client = beneath.Client(secret=secret)
    return client


async def get_stream(username, project, stream):
    client = await get_client()
    stream = await client.find_stream(stream_path=f'{username}/{project}/{stream}')
    await client.stop()
    return stream
