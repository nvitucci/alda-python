from collections import OrderedDict
from typing import Any, BinaryIO, Dict, List, Optional, Union

STRING_LEN_DELIMITER = b":"
INT_START_DELIMITER = b"i"
LIST_START_DELIMITER = b"l"
DICT_START_DELIMITER = b"d"
END_DELIMITER = b"e"

BencodeType = Union[str, bytes, int, List[Any], Dict[str, Any]]


class Bencode:
    def __init__(self, f: BinaryIO) -> None:
        self.f = f

    def read(self) -> Optional[BencodeType]:
        data = self.f.read(1)

        if data == INT_START_DELIMITER:
            return self.read_int()
        elif data == LIST_START_DELIMITER:
            return self.read_list()
        elif data == DICT_START_DELIMITER:
            return self.read_dict()
        elif data == END_DELIMITER:
            return None
        else:
            return self.read_string(data)

    def read_string_length(self, initial: bytes) -> int:
        return self.read_int(initial, STRING_LEN_DELIMITER)

    def read_int(self, initial: Optional[bytes] = None, delimiter: bytes = END_DELIMITER) -> int:
        data = bytes()

        if initial is not None:
            data += initial

        while (r := self.f.read(1)) != delimiter:
            data += r

        return int(data)

    def read_string(self, initial: bytes) -> Union[str, bytes]:
        length = self.read_string_length(initial)
        data = bytes()

        while len(data) < length:
            data += self.f.read(length - len(data))

        try:
            return data.decode()
        except UnicodeDecodeError:
            return data

    def read_list(self) -> List[Any]:
        data = []

        while (r := self.read()) is not None:
            data.append(r)

        return data

    def read_dict(self) -> Dict[str, Any]:
        data = self.read_list()

        item = iter(data)
        return OrderedDict(zip(item, item))

    def write(self, obj: BencodeType) -> None:
        encoded = self.encode(obj)

        self.f.write(encoded)
        self.f.flush()

    @classmethod
    def encode(cls, obj: BencodeType) -> bytes:
        if isinstance(obj, str):
            return f"{len(obj)}:{obj}".encode()
        elif isinstance(obj, bytes):
            return f"{len(obj)}:".encode() + obj
        elif isinstance(obj, int):
            return f"i{obj}e".encode()
        elif isinstance(obj, (list, tuple)):
            data = b"".join(Bencode.encode(el) for el in obj)
            # Cannot use f-strings because the 'b' gets included too
            return b"l" + data + b"e"
        elif isinstance(obj, dict):
            data = b"".join(Bencode.encode(k) + Bencode.encode(v) for k, v in obj.items())
            return b"d" + data + b"e"
