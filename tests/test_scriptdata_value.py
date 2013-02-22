# vim: set fileencoding=utf8 :

from __future__ import unicode_literals

from flashmedia.types import (ScriptDataDate,
                              ScriptDataReference,
                              ScriptDataECMAArray,
                              ScriptDataObject,
                              ScriptDataValue)

BOOL = b"\x01\x01"
BOOL_SIZE = len(BOOL)

NULL = b"\x05"
NULL_SIZE = len(NULL)

NUMBER = b"\x00@b\xd0\x00\x00\x00\x00\x00"
NUMBER_SIZE = len(NUMBER)

STRICT_ARRAY = b"\n\x00\x00\x00\x00"
STRICT_ARRAY_SIZE = len(STRICT_ARRAY)

ECMA_ARRAY = b"\x08\x00\x00\x00\x00\x00\x00\t"
ECMA_ARRAY_SIZE = len(ECMA_ARRAY)

OBJECT = b"\x03\x00\x00\t"
OBJECT_SIZE = len(OBJECT)

STRING = b"\x02\x00\x03ABC"
STRING_SIZE = len(STRING)

DATE = b"\x0b@\xfe$\x00\x00\x00\x00\x00\xff\xff"
DATE_SIZE = len(DATE)

REFERENCE = b"\x07\x00/"
REFERENCE_SIZE = len(REFERENCE)

def create_date():
    return ScriptDataDate(123456.0, -1)

def create_reference():
    return ScriptDataReference(47)

def test_pack():
    assert ScriptDataValue(True) == BOOL
    assert ScriptDataValue(None) == NULL
    assert ScriptDataValue(150.5) == NUMBER
    assert ScriptDataValue([]) == STRICT_ARRAY
    assert ScriptDataValue(ScriptDataECMAArray()) == ECMA_ARRAY
    assert ScriptDataValue(ScriptDataObject()) == OBJECT
    assert ScriptDataValue("ABC") == STRING
    assert ScriptDataValue(create_date()) == DATE
    assert ScriptDataValue(create_reference()) == REFERENCE

def test_unpack():
    assert ScriptDataValue.unpack(BOOL)[0] == True
    assert ScriptDataValue.unpack(NULL)[0] == None
    assert ScriptDataValue.unpack(NUMBER)[0] == 150.5
    assert ScriptDataValue.unpack(STRICT_ARRAY)[0] == []
    assert ScriptDataValue.unpack(ECMA_ARRAY)[0] == ScriptDataECMAArray()
    assert ScriptDataValue.unpack(OBJECT)[0] == ScriptDataObject()
    assert ScriptDataValue.unpack(STRING)[0] == "ABC"
    assert ScriptDataValue.unpack(DATE)[0] == create_date()
    assert ScriptDataValue.unpack(REFERENCE)[0] == create_reference()

def test_size():
    assert ScriptDataValue.size(True) == BOOL_SIZE
    assert ScriptDataValue.size(None) == NULL_SIZE
    assert ScriptDataValue.size(150.5) == NUMBER_SIZE
    assert ScriptDataValue.size([]) == STRICT_ARRAY_SIZE
    assert ScriptDataValue.size(ScriptDataECMAArray()) == ECMA_ARRAY_SIZE
    assert ScriptDataValue.size(ScriptDataObject()) == OBJECT_SIZE
    assert ScriptDataValue.size("ABC") == STRING_SIZE
    assert ScriptDataValue.size(create_date()) == DATE_SIZE
    assert ScriptDataValue.size(create_reference()) == REFERENCE_SIZE

