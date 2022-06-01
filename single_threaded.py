import hashlib
import time
from random import randbytes
from typing import Optional, List


def mine(target_len: int) -> Optional[bytes]:
    max_attempts = 1000000
    success = "0" * target_len
    attempts = 0
    while attempts < max_attempts:
        h = hashlib.new("sha256")
        attempt = randbytes(100)
        h.update(attempt)
        hashed = h.hexdigest()
        if hashed[-target_len:] == success:
            print(f"Took {attempts} attempts")
            return attempt
        attempts += 1

    return None


def mine_multiple(successes_desired: int, target_len: int) -> List[bytes]:
    successes = []
    while len(successes) < successes_desired:
        res = mine(target_len=target_len)
        if res is not None:
            successes.append(res)

    return successes


if __name__ == "__main__":
    start = time.time()
    target_len = 4

    successes_desired = 100
    successes = mine_multiple(successes_desired, target_len)

    # Let's make sure our workers didn't misbehave!
    success = "0" * target_len
    for text in successes:
        h = hashlib.new("sha256")
        h.update(text)
        hashed = h.hexdigest()
        assert hashed[-target_len:] == success

    end = time.time()
    print(f"Generated {len(successes)} hashes in {end-start}s")
