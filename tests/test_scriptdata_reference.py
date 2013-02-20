from flashmedia.types import ScriptDataReference, ScriptDataReferenceStruct
from nose.tools import *

BYTES = b"\x00\x01"

def test_pack():
    val = ScriptDataReference(1)
    assert ScriptDataReferenceStruct.pack(val) == BYTES

def test_unpack():
    val = ScriptDataReferenceStruct.unpack(BYTES)[0]

    assert isinstance(val, ScriptDataReference)
    assert val.reference == 1

def test_unpack_from():
    buf = BYTES * 2
    offset = 0
    val = ScriptDataReferenceStruct.unpack_from(buf, offset)[0]

    assert isinstance(val, ScriptDataReference)
    assert val.reference == 1
