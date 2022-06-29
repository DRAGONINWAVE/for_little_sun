from ast import Str
import time
from pathlib import Path
#from tty import CC
from typing import Callable

import requests

POP20_CC = ('CN IN US BR').split()
BASE_URL = 'http://fluentpython.com/data/flags'
DEST_DIR = Path('downloaded')

def save_flag(img:bytes,filename:str) -> None:
    (DEST_DIR / filename).write_bytes(img)

def get_flag(cc: str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = requests.get(url)
    return resp.content


def download_many(cc_list:list[str]) -> int:
    for cc in sorted(cc_list):
        image = get_flag(cc)
        save_flag(image,f'{cc}.gif')
        print(cc,end=' ',flush = True)
    return len(cc_list)

def main(downloader:Callable[[list[str]],int]) -> None:
    t0 = time.perf_counter()
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f'\n{count} downloads in {elapsed:.2f}s')

if __name__ == '__main__':
    main(download_many)
