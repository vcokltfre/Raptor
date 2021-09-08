from os import environ as env
from time import time


class IDGenerator:
    def __init__(self) -> None:
        self.wid = 0
        self.inc = 0

    def next(self) -> int:
        t = round(time() * 1000) - 1609459200000
        self.inc += 1
        return (t << 14) | (self.wid << 6) | (self.inc % 2 ** 6)


_gen = IDGenerator()


def create_snowflake() -> int:
    return _gen.next()
