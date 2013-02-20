from flashmedia.types import FourCC
from nose.tools import *


def test_pack():
    assert FourCC("A")     == b"A   "
    assert FourCC("AB")    == b"AB  "
    assert FourCC("ABC")   == b"ABC "
    assert FourCC("ABCD")  == b"ABCD"

def test_pack_overflow():
    assert FourCC("ABCDE") == b"ABCD"

def test_unpack():
    assert FourCC.unpack(b"A   ")[0] == "A"
    assert FourCC.unpack(b"AB  ")[0] == "AB"
    assert FourCC.unpack(b"ABC ")[0] == "ABC"
    assert FourCC.unpack(b"ABCD")[0] == "ABCD"

def test_unpack_from():
    assert FourCC.unpack_from(b"A   ", 0)[0] == "A"
    assert FourCC.unpack_from(b"AB  ", 0)[0] == "AB"
    assert FourCC.unpack_from(b"ABC ", 0)[0] == "ABC"
    assert FourCC.unpack_from(b"ABCD", 0)[0] == "ABCD"
