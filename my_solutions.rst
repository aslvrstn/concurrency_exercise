-------------
test_pings.py
-------------

My solution::

    def get_pings(urls: List[str]) -> Dict[str, int]:
        with ThreadPoolExecutor() as tpe:
            res = tpe.map(get_ping, urls)
            return {url: ping for url, ping in zip(urls, res)}

Using gevent::

    # This is kind of a magic incantation that must run before any other imports
    from gevent import monkey; monkey.patch_all()
    from gevent import Greenlet

    def get_pings(urls: List[str]) -> Dict[str, int]:
        glets = []
        for url in urls:
            glets.append(Greenlet.spawn(get_ping, url))

        return {url: glet.get() for url, glet in zip(urls, glets)}

-------------
mine.py
-------------

My solution::

    def mine_multiple(successes_desired: int, target_len: int) -> List[bytes]:
        successes = []
        with ProcessPoolExecutor() as ppe:
            miners = []

            for i in range(successes_desired):
                miners.append(ppe.submit(mine, target_len))

            for miner in miners:
                res = miner.result()
                if res is not None:
                    successes.append(res)
                else:
                    # This miner failed to find one! Try again
                    miners.append(ppe.submit(mine, target_len))

        return successes