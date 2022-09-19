from collections import OrderedDict

STRING_LEN_DELIMITER = b":"
INT_START_DELIMITER = b"i"
LIST_START_DELIMITER = b"l"
DICT_START_DELIMITER = b"d"
END_DELIMITER = b"e"


class Bencode:
    f = None

    def __init__(self, f):
        self.f = f

    def read(self):
        data = self.f.read(1)

        if data == INT_START_DELIMITER:
            data = self.read_int()
        elif data == LIST_START_DELIMITER:
            data = self.read_list()
        elif data == DICT_START_DELIMITER:
            data = self.read_dict()
        elif data == END_DELIMITER:
            return None
        else:
            data = self.read_string(data)

        return data

    def read_string_length(self, initial):
        return self.read_int(initial, STRING_LEN_DELIMITER)

    # NOTE: This skips negative integers
    def read_int(self, initial=None, delimiter=END_DELIMITER):
        data = bytes()

        if initial is not None:
            data += initial

        while (r := self.f.read(1)).isdigit():
            data += r
        assert r == delimiter, f"Wrong delimiter: {r}, should be {delimiter}"

        return int(data)

    def read_string(self, initial):
        length = self.read_string_length(initial)
        data = bytes()

        while len(data) < length:
            data += self.f.read(length - len(data))

        assert len(data) == length, "Wrong string length"
        return data

    def read_list(self):
        data = []

        while (r := self.read()) is not None:
            data.append(r)

        return data

    def read_dict(self):
        data = self.read_list()

        item = iter(data)
        return OrderedDict(zip(item, item))

    def write(self, obj):
        encoded = self.encode(obj)

        self.f.write(encoded.encode())
        self.f.flush()

    def encode(self, obj):
        if isinstance(obj, (str, bytes)):
            return f"{len(obj)}:{obj}"
        elif isinstance(obj, int):
            return f"i{obj}e"
        elif isinstance(obj, (list, tuple)):
            data = "".join(self.encode(el) for el in obj)
            return f"l{data}e"
        elif isinstance(obj, dict):
            data = "".join(self.encode(k) + self.encode(v) for k, v in obj.items())
            return f"d{data}e"
