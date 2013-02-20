# vim: set fileencoding=utf8 :

from . import with_fd
from nose.tools import *

from flashmedia.types import ScriptDataECMAArray

EMPTY_ARRAY = b"\x00\x00\x00\x00\x00\x00\t"
EMPTY_ARRAY_SIZE = len(EMPTY_ARRAY)

NUMBER_VALUE = b"\x00\x00\x00\x01\x00\x03foo\x00@^\xc0\x00\x00\x00\x00\x00\x00\x00\t"
NUMBER_VALUE_SIZE = len(NUMBER_VALUE)

STRING_VALUE = b"\x00\x00\x00\x01\x00\x03foo\x02\x00\x03bar\x00\x00\t"
STRING_VALUE_SIZE = len(STRING_VALUE)

BOOLEAN_VALUE = b"\x00\x00\x00\x01\x00\x03foo\x01\x01\x00\x00\t"
BOOLEAN_VALUE_SIZE = len(BOOLEAN_VALUE)

MIXED_VALUES = b"\x00\x00\x00\x03\x00\x06number\x00@^\xc0\x00\x00\x00\x00\x00\x00\x06string\x02\x00\x06foobar\x00\x04bool\x01\x01\x00\x00\t"
MIXED_VALUES_SIZE = len(MIXED_VALUES)

def create_mixed_array():
    obj = ScriptDataECMAArray()

    # Preserves insertion order
    obj["number"] = 123
    obj["string"] = "foobar"
    obj["bool"] = True

    return obj

def test_pack_empty_array():
    assert ScriptDataECMAArray.pack(ScriptDataECMAArray()) == EMPTY_ARRAY

def test_pack_numbers_array():
    assert ScriptDataECMAArray.pack(ScriptDataECMAArray(foo=123)) == NUMBER_VALUE

def test_pack_strings_array():
    assert ScriptDataECMAArray.pack(ScriptDataECMAArray(foo="bar")) == STRING_VALUE

def test_pack_booleans_array():
    assert ScriptDataECMAArray.pack(ScriptDataECMAArray(foo=True)) == BOOLEAN_VALUE

def test_pack_mixed_array():
    obj = create_mixed_array()

    assert ScriptDataECMAArray.pack(obj) == MIXED_VALUES

def test_pack_into_mixed_array():
    obj = create_mixed_array()
    size = ScriptDataECMAArray.size(obj)
    buf = bytearray(size)
    offset = 0

    assert ScriptDataECMAArray.pack_into(buf, offset, obj) == MIXED_VALUES_SIZE
    

def test_size_empty_array():
    assert ScriptDataECMAArray.size(ScriptDataECMAArray()) == EMPTY_ARRAY_SIZE

def test_size_numbers_array():
    assert ScriptDataECMAArray.size(ScriptDataECMAArray(foo=123)) == NUMBER_VALUE_SIZE

def test_size_strings_array():
    assert ScriptDataECMAArray.size(ScriptDataECMAArray(foo="bar")) == STRING_VALUE_SIZE

def test_size_booleans_array():
    assert ScriptDataECMAArray.size(ScriptDataECMAArray(foo=True)) == BOOLEAN_VALUE_SIZE

def test_size_mixed_array():
    obj = create_mixed_array()

    assert ScriptDataECMAArray.size(obj) == MIXED_VALUES_SIZE


@with_fd(EMPTY_ARRAY)
def test_read_empty_array(fd):
    assert ScriptDataECMAArray.read(fd) == ScriptDataECMAArray()
    assert fd.tell() == EMPTY_ARRAY_SIZE

@with_fd(NUMBER_VALUE)
def test_read_numbers_array(fd):
    assert ScriptDataECMAArray.read(fd) == ScriptDataECMAArray(foo=123)
    assert fd.tell() == NUMBER_VALUE_SIZE

@with_fd(STRING_VALUE)
def test_read_strings_array(fd):
    assert ScriptDataECMAArray.read(fd) == ScriptDataECMAArray(foo="bar")
    assert fd.tell() == STRING_VALUE_SIZE

@with_fd(BOOLEAN_VALUE)
def test_read_booleans_array(fd):
    assert ScriptDataECMAArray.read(fd) == ScriptDataECMAArray(foo=True)
    assert fd.tell() == BOOLEAN_VALUE_SIZE

@with_fd(MIXED_VALUES)
def test_read_mixed_array(fd):
    obj = create_mixed_array()

    assert ScriptDataECMAArray.read(fd) == obj
    assert fd.tell() == MIXED_VALUES_SIZE

def test_unpack_from():
    obj = create_mixed_array()
    buf = MIXED_VALUES * 2
    offset = 0

    assert ScriptDataECMAArray.unpack_from(buf, offset) == (obj, MIXED_VALUES_SIZE)


