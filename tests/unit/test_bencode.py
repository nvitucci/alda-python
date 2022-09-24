from io import BytesIO
from typing import Any

import pytest

from alda import Bencode

VALUES = [
    (b"0:", ""),
    (b"4:spam", "spam"),
    (b"1024:" + (b"a" * 1024), "a" * 1024),
    (b"10240:" + (b"a" * 10240), "a" * 10240),
    (b"i3e", 3),
    (b"i-3e", -3),
    (b"le", []),
    (b"l4:spam4:eggse", ["spam", "eggs"]),
    (b"l4:spam4:eggsd3:cow3:mooee", ["spam", "eggs", {"cow": "moo"}]),
    (b"d3:cow3:moo4:spam4:eggse", {"cow": "moo", "spam": "eggs"}),
    (
        b"d9:publisher3:bob17:publisher-webpage15:www.example.com18:publisher.location4:homee",
        {"publisher": "bob", "publisher-webpage": "www.example.com", "publisher.location": "home"},
    ),
    (b"d3:cow3:moo4:spaml1:a1:bee", {"cow": "moo", "spam": ["a", "b"]}),
    (b"d3:cow3:moo4:spamd1:a1:bee", {"cow": "moo", "spam": {"a": "b"}}),
    (
        b"33:MThd\x00\x00\x00\x06\x00\x00\x00\x01\x00\x80MTrk\x00\x00\x00\x0b\x00\xffQ\x03\x07\xa1 \x00\xff/\x00",
        b"MThd\x00\x00\x00\x06\x00\x00\x00\x01\x00\x80MTrk\x00\x00\x00\x0b\x00\xffQ\x03\x07\xa1 \x00\xff/\x00"
    )
]


class TestBencodeRead:
    @pytest.mark.parametrize("encoded, decoded", VALUES)
    def test_values(self, encoded: bytes, decoded: Any) -> None:
        b = Bencode(BytesIO(encoded))
        assert b.read() == decoded


class TestBencodeWrite:
    @pytest.mark.parametrize("encoded, decoded", VALUES)
    def test_values(self, encoded: bytes, decoded: Any) -> None:
        buffer = BytesIO()
        b = Bencode(buffer)
        b.write(decoded)

        buffer.seek(0)
        assert buffer.read() == encoded
