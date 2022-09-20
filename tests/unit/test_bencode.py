import pytest

from io import BytesIO

from alda.bencode import Bencode

VALUES = [
    ("0:", b""),
    ("4:spam", b"spam"),
    ("i3e", 3),
    ("le", []),
    ("l4:spam4:eggse", [b"spam", b"eggs"]),
    ("l4:spam4:eggsd3:cow3:mooee", [b"spam", b"eggs", {b"cow": b"moo"}]),
    ("de", {}),
    ("d3:cow3:moo4:spam4:eggse", {b"cow": b"moo", b"spam": b"eggs"}),
    ("d9:publisher3:bob17:publisher-webpage15:www.example.com18:publisher.location4:homee",
        {b"publisher": b"bob", b"publisher-webpage": b"www.example.com", b"publisher.location": b"home"}),
    ("d3:cow3:moo4:spaml1:a1:bee", {b"cow": b"moo", b"spam": [b"a", b"b"]}),
]

# TODO: there should be no difference with VALUES
VALUES_NO_BIN = [
    ("0:", ""),
    ("4:spam", "spam"),
    ("i3e", 3),
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
    @pytest.mark.parametrize("encoded, decoded", VALUES_NO_BIN)
    def test_values(self, encoded, decoded):
        buffer = BytesIO()
        b = Bencode(buffer)
        b.write(decoded)

        buffer.seek(0)
        assert buffer.read().decode() == encoded
