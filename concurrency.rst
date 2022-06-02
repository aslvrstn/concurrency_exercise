So you need to learn about concurrency in python, you poor soul.

OK, well, here's a starter challenge.

#. Modify `test_pings.py` to run in under two seconds. On my machine it currently takes about six seconds.

#. Modify `mine.py` to run in under two seconds. On my machine it currently takes about six seconds.

#. Check out the results of `viztracer --min_duration=1000 test_pings.py` and `viztracer --min_duration=1000 mine.py` in `vizviewer`.

==============
More details
==============
Alex rambles for a bit before incorporating this into the text eventually.

-------------
test_pings.py
-------------

`test_pings.py` is pretty straightforward. Find the time to load a small set of websites. Hint: we should be able to do this about as quickly as it takes to load the slowest website.


-------------
mine.py
-------------

`mine.py` is a very crude simulation of bitcoin mining. Why? Well, literally the whole point of bitcoin mining is that it's CPU-intensive, and for the purposes of this exercise, we want a CPU-intensive python methods. (This is also a hint!) If bitcoin can burn cycles to run a itty bitty database, we can certainly do it for education!

In very brief, mining is the following:
For a given difficulty, `d`, find a string, `s`, such that `sha256(s)` ends with `d` zeroes. So, for example:

>>> import hashlib
>>> h = hashlib.new("sha256")
>>> h.update("6r2qKCH48MKM+iqWST9BwXPInLDzmxkIhr4rUf0RfLSy5KmUFjaIUHiXD7IztaA95qT4O40gqsgj0ROsNwgALZgdnrQ7Wc4VeeFKy8i/0WD3soFEsjPWHM6HgzIkP5zWRYS0rw==".encode("ascii"))
>>> h.hexdigest()
'f759532e145f89d83da2d78bfa97d08de783a05200e542a54b07a9d06ff30000'

means that that long string starting with `6r2qK...` is a successful mine of difficulty 4, since its hash ends in `...ff30000`.

The point of this is that there is no better way to generate successes like this other than to try hashing a random string and hoping you get lucky.