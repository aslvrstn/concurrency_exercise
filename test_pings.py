import time
from typing import List, Dict

import requests


def get_ping(url: str) -> int:
    """Return the number of milliseconds it takes to load `url`"""
    return int(requests.get(url).elapsed.microseconds / 1000)


def get_pings(urls: List[str]) -> Dict[str, int]:
    """Return a map from url to its ping"""
    return {url: get_ping(url) for url in urls}


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