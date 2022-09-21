import pytest

from io import BytesIO

from alda.bencode import Bencode

VALUES = [
    ("0:", ""),
    ("4:spam", "spam"),
    ("1024:" + ("a" * 1024), "a" * 1024),
    ("10240:" + ("a" * 10240), "a" * 10240),
    ("i3e", 3),
    ("i-3e", -3),
    ("le", []),
    ("l4:spam4:eggse", ["spam", "eggs"]),
    ("l4:spam4:eggsd3:cow3:mooee", ["spam", "eggs", {"cow": "moo"}]),
    ("d3:cow3:moo4:spam4:eggse", {"cow": "moo", "spam": "eggs"}),
    ("d9:publisher3:bob17:publisher-webpage15:www.example.com18:publisher.location4:homee",
        {"publisher": "bob", "publisher-webpage": "www.example.com", "publisher.location": "home"}),
    ("d3:cow3:moo4:spaml1:a1:bee", {"cow": "moo", "spam": ["a", "b"]}),
    ("d3:cow3:moo4:spamd1:a1:bee", {"cow": "moo", "spam": {"a": "b"}}),
]


class TestBencodeRead:
    @pytest.mark.parametrize("encoded, decoded", VALUES)
    def test_values(self, encoded, decoded):
        b = Bencode(BytesIO(encoded.encode()))
        assert b.read() == decoded

    @pytest.mark.skip
    def test_neg_int(self):
        value = "i-3e"

        with pytest.raises(AssertionError):
            Bencode(BytesIO(value.encode()))


class TestBencodeWrite:
    @pytest.mark.parametrize("encoded, decoded", VALUES)
    def test_values(self, encoded, decoded):
        buffer = BytesIO()
        b = Bencode(buffer)
        b.write(decoded)

        buffer.seek(0)
        assert buffer.read().decode() == encoded
