import requests
import os


async def download_file(url, local_filename):
    response = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    return local_filename


async def delete_file(local_filename):
    if os.path.exists(local_filename):
        os.remove(local_filename)
