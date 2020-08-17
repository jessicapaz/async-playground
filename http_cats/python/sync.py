import requests
import logging
import os
import time
from http import HTTPStatus


logging.basicConfig(level=logging.DEBUG)


def download_image(status):
    url = f'https://http.cat/{status}.jpg'
    response = requests.get(url)
    if response.status_code == HTTPStatus.OK:
        filename = os.path.join(os.getcwd(), 'imgs', f'{status}.jpg')
        with open(filename, 'wb') as f:
            f.write(response.content)


def download_all_images():
    for status in HTTPStatus:
        download_image(status.value)


if __name__ == '__main__':
    os.mkdir('imgs')
    logging.info(f'started at {time.strftime("%X")}')
    download_all_images()
    logging.info(f'finished at {time.strftime("%X")}')
