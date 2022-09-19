import socket

import nrepl

from .bencode import Bencode


class NREPLClient:
    client = None

    def __init__(self, host, port):
        conn_string = f"nrepl://{host}:{port}"
        self.client = nrepl.connect(conn_string)

    def write(self, message):
        return self.client.write(message)

    def read(self):
        return self.client.read()

    def close(self):
        return self.client.close()


class CustomNREPLClient:
    conn = None
    f = None
    bencode = None

    def __init__(self, host, port):
        self.conn = socket.create_connection(address=(host, port))
        self.f = self.conn.makefile("rwb")
        self.bencode = Bencode(self.f)

    def write(self, message):
        return self.bencode.write(message)

    def read(self):
        return self.bencode.read()

    def close(self):
        self.conn.shutdown(socket.SHUT_RDWR)
        self.conn.close()
        self.f.close()
