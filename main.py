from time import sleep
from lib.data.movies import write_data
from lib.streams.movies import create_stream


if __name__ == '__main__':
    create_stream()

    # Keep sending events every second to mock live behavior
    while True:
        write_data()
        sleep(1)
        
