import socket
from typing import Any, BinaryIO, Dict

from .bencode import Bencode


class NREPLClient:
    def __init__(self, host: str, port: int):
        self.conn: Any = socket.create_connection(address=(host, port))
        self.f: BinaryIO = self.conn.makefile("rwb")
        self.bencode = Bencode(self.f)

    def write(self, message: Dict[str, Any]) -> None:
        self.bencode.write(message)

    def read(self) -> Dict[str, Any]:
        response = self.bencode.read()

        if not isinstance(response, dict):
            raise ValueError("Wrong type for response", response)

        return response

    def close(self) -> None:
        self.conn.shutdown(socket.SHUT_RDWR)
        self.conn.close()
        self.f.close()
