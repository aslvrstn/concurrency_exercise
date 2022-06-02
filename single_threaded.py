import hashlib
import time
from random import randbytes
from typing import Optional, List


def mine(target_len: int) -> Optional[bytes]:
    """Generate a single string whose sha256 hash ends with `target_len` zeroes.

    This function should not be modified in your solution!

    :param target_len: aka difficulty. How many zeroes does a success need to end with?
    :return: a successful input, or None if we bailed before finding one
    """
    # How many times do we try to find a solution before we bail
    max_attempts = 100000
    # A successful attempt's hash ends with `target_len` zeroes
    success = "0" * target_len
    attempts = 0
    while attempts < max_attempts:
        h = hashlib.new("sha256")
        # Generate a random input as a potential solution
        attempt = randbytes(100)
        h.update(attempt)
        hashed = h.hexdigest()

        # And check whether the hash ends with the requisite string (number of zeroes)
        if hashed[-target_len:] == success:
            print(f"Took {attempts} attempts")
            return attempt
        attempts += 1

    print(f"No solution found after {max_attempts} tries")
    return None


def mine_multiple(successes_desired: int, target_len: int) -> List[bytes]:
    """Generate `success_desired` strings whose sha256 hash ends with `target_len` zeroes.

    This is the function that we want to modify to speed up our mining!

    :param successes_desired: the number of strings to find
    :param target_len: aka difficulty. How many zeroes does a success need to end with?
    :return: a list of length `successes_desired` successful strings
    """
    successes: List[bytes] = []
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

    if len(successes) < successes_desired:
        raise AssertionError(f"Wanted {successes_desired} successes but only got {len(successes)}")

    # Make sure no one is sneaky and tries to return the same result multiple times
    if len(set(successes)) < successes_desired:
        raise AssertionError("Successes weren't unique. What're you trying to pull here...")
