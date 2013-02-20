from flashmedia.types import ScriptDataDate, ScriptDataDateStruct
from nose.tools import *

BYTES = b"@\xfe$\x00\x00\x00\x00\x00\xff\xff"
BYTES_SIZE = len(BYTES)

def test_pack():
    val = ScriptDataDate(123456.0, -1)
    assert ScriptDataDateStruct.pack(val) == BYTES

def test_unpack():
    val = ScriptDataDateStruct.unpack(BYTES)[0]

    assert isinstance(val, ScriptDataDate)
    assert val.timestamp == 123456.0
    assert val.offset == -1

def test_unpack_from():
    buf = BYTES * 2
    offset = 0
    val = ScriptDataDateStruct.unpack_from(buf, offset)[0]

    assert isinstance(val, ScriptDataDate)
    assert val.timestamp == 123456.0
    assert val.offset == -1
