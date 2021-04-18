import os
import beneath

from dotenv import load_dotenv


USERNAME = 'sarahmk125'
SECRETS_FILE = 'secrets.env'


def get_client():
    load_dotenv(SECRETS_FILE)
    secret = os.getenv('BENEATH_SECRET')
    client = beneath.Client(secret=secret)
    return client
