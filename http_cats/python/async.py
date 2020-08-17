import aiohttp
import asyncio
import logging
import os
import time
from http import HTTPStatus


logging.basicConfig(level=logging.DEBUG)


async def download_image(status):
    url = f'https://http.cat/{status}.jpg'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == HTTPStatus.OK:
                content = await response.read()
                filename = os.path.join(os.getcwd(), 'imgs', f'{status}.jpg')
                with open(filename, 'wb') as f:
                    f.write(content)


async def download_all_images():
    await asyncio.gather(
        *[download_image(status.value) for status in HTTPStatus]
    )

if __name__ == '__main__':
    os.mkdir('imgs')
    logging.info(f'started at {time.strftime("%X")}')
    asyncio.run(download_all_images())
    logging.info(f'finished at {time.strftime("%X")}')
