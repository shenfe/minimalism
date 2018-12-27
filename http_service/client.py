# coding: utf8

import requests


class Client:

    def __init__(self, origin):
        self.origin = origin
        self.s = requests.Session()

    def process(self, data):
        r = self.s.post(self.origin, json=data)
        assert r.status_code == 200
        return r.json()


if __name__ == '__main__':

    cli = Client('http://127.0.0.1:4000')
    print cli.process({'hello': 'world'})
    print cli.process([1, 2, 3, 4])
