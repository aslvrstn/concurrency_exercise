import time
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict

import requests


def get_ping(url: str) -> int:
    return int(requests.get(url).elapsed.microseconds / 1000)


def get_pings(urls: List[str]) -> Dict[str, int]:
    with ThreadPoolExecutor() as tpe:
        res = tpe.map(get_ping, urls)
        return {url: ping for url, ping in zip(urls, res)}


if __name__ == "__main__":
    urls = [
        "https://google.com",
        "https://yahoo.com",
        "https://wikipedia.com",
        "https://www.pythonlikeyoumeanit.com/",
        "https://aslvrstn.com/",
        "https://www.smithfieldfoods.com/",
        "https://www.t-sg.jp/en/",
    ]
    start = time.time()
    res = get_pings(urls)
    end = time.time()

    print(res)
    print(f"Got {len(urls)} pings in {end-start}s")