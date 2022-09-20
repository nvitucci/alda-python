import pytest

from io import BytesIO

from alda.bencode import Bencode


class TestBencodeRead:
    def test_empty_string(self):
        value = "0:"

        b = Bencode(BytesIO(value.encode()))
        assert b.read() == b""

    def test_string(self):
        value = "4:spam"

        b = Bencode(BytesIO(value.encode()))
        assert b.read() == b"spam"

    def test_int(self):
        value = "i3e"

        b = Bencode(BytesIO(value.encode()))
        assert b.read() == 3

    @pytest.mark.skip
    def test_neg_int(self):
        value = "i-3e"

        with pytest.raises(AssertionError):
            Bencode(BytesIO(value.encode()))

    def test_empty_list(self):
        value = "le"

        b = Bencode(BytesIO(value.encode()))
        assert b.read() == []

    def test_simple_list(self):
        value = "l4:spam4:eggse"

        b = Bencode(BytesIO(value.encode()))
        assert b.read() == [b"spam", b"eggs"]

    def test_list_with_dic(self):
        value = "l4:spam4:eggsd3:cow3:mooee"

        b = Bencode(BytesIO(value.encode()))
        assert b.read() == [b"spam", b"eggs", {b"cow": b"moo"}]

    def test_empty_dic(self):
        value = "dev"

        b = Bencode(BytesIO(value.encode()))
        assert b.read() == {}

    def test_simple_dic(self):
        value = "d3:cow3:moo4:spam4:eggse"

        b = Bencode(BytesIO(value.encode()))
        assert b.read() == {b"cow": b"moo", b"spam": b"eggs"}

    def test_larger_dic(self):
        value = "d9:publisher3:bob17:publisher-webpage15:www.example.com18:publisher.location4:homee"

        b = Bencode(BytesIO(value.encode()))
        assert b.read() == {b"publisher": b"bob", b"publisher-webpage": b"www.example.com", b"publisher.location": b"home"}

    def test_dic_with_list(self):
        value = "d3:cow3:moo4:spaml1:a1:beee"

        b = Bencode(BytesIO(value.encode()))
        assert b.read() == {b"cow": b"moo", b"spam": [b"a", b"b"]}

    def test_dic_with_dic(self):
        value = "d3:cow3:moo4:spamd1:a1:beee"

        b = Bencode(BytesIO(value.encode()))
        assert b.read() == {b"cow": b"moo", b"spam": {b"a": b"b"}}
