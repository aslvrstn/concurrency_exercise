import hashlib
from random import randbytes

def mine():
    target_len = 5
    max_attempts = 1000000
    success = "0" * target_len
    attempts = 0
    while attempts < max_attempts:
        h = hashlib.new('sha256')
        attempt = randbytes(100)
        h.update(attempt)
        hashed = h.hexdigest()
        if hashed[-target_len:] == success:
            print(h.hexdigest())
            print(f"Took {attempts} attempts")
            return attempt
        attempts += 1

    return None

if __name__ == "__main__":
    mine()
