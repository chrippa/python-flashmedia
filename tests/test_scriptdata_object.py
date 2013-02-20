# vim: set fileencoding=utf8 :

from . import with_fd
from nose.tools import *

from flashmedia.types import ScriptDataObject

EMPTY_OBJECT = b"\x00\x00\t"
EMPTY_OBJECT_SIZE = len(EMPTY_OBJECT)

NUMBER_VALUE = b"\x00\x03foo\x00@^\xc0\x00\x00\x00\x00\x00\x00\x00\t"
NUMBER_VALUE_SIZE = len(NUMBER_VALUE)

STRING_VALUE = b"\x00\x03foo\x02\x00\x03bar\x00\x00\t"
STRING_VALUE_SIZE = len(STRING_VALUE)

BOOLEAN_VALUE = b"\x00\x03foo\x01\x01\x00\x00\t"
BOOLEAN_VALUE_SIZE = len(BOOLEAN_VALUE)

MIXED_VALUES = b"\x00\x06number\x00@^\xc0\x00\x00\x00\x00\x00\x00\x06string\x02\x00\x06foobar\x00\x04bool\x01\x01\x00\x00\t"
MIXED_VALUES_SIZE = len(MIXED_VALUES)


def test_pack_empty_object():
    assert ScriptDataObject.pack(ScriptDataObject()) == EMPTY_OBJECT

def test_pack_numbers_object():
    assert ScriptDataObject.pack(ScriptDataObject(foo=123)) == NUMBER_VALUE

def test_pack_strings_object():
    assert ScriptDataObject.pack(ScriptDataObject(foo="bar")) == STRING_VALUE

def test_pack_booleans_object():
    assert ScriptDataObject.pack(ScriptDataObject(foo=True)) == BOOLEAN_VALUE

def test_pack_mixed_object():
    obj = ScriptDataObject()

    # Preserves insertion order
    obj["number"] = 123
    obj["string"] = "foobar"
    obj["bool"] = True

    assert ScriptDataObject.pack(obj) == MIXED_VALUES


def test_size_empty_object():
    assert ScriptDataObject.size(ScriptDataObject()) == EMPTY_OBJECT_SIZE

def test_size_numbers_object():
    assert ScriptDataObject.size(ScriptDataObject(foo=123)) == NUMBER_VALUE_SIZE

def test_size_strings_object():
    assert ScriptDataObject.size(ScriptDataObject(foo="bar")) == STRING_VALUE_SIZE

def test_size_booleans_object():
    assert ScriptDataObject.size(ScriptDataObject(foo=True)) == BOOLEAN_VALUE_SIZE

def test_size_mixed_object():
    obj = ScriptDataObject()

    # Preserves insertion order
    obj["number"] = 123
    obj["string"] = "foobar"
    obj["bool"] = True

    assert ScriptDataObject.size(obj) == MIXED_VALUES_SIZE


@with_fd(EMPTY_OBJECT)
def test_read_empty_object(fd):
    assert ScriptDataObject.read(fd) == ScriptDataObject()
    assert fd.tell() == EMPTY_OBJECT_SIZE

@with_fd(NUMBER_VALUE)
def test_read_numbers_object(fd):
    assert ScriptDataObject.read(fd) == ScriptDataObject(foo=123)
    assert fd.tell() == NUMBER_VALUE_SIZE

@with_fd(STRING_VALUE)
def test_read_strings_object(fd):
    assert ScriptDataObject.read(fd) == ScriptDataObject(foo="bar")
    assert fd.tell() == STRING_VALUE_SIZE

@with_fd(BOOLEAN_VALUE)
def test_read_booleans_object(fd):
    assert ScriptDataObject.read(fd) == ScriptDataObject(foo=True)
    assert fd.tell() == BOOLEAN_VALUE_SIZE

@with_fd(MIXED_VALUES)
def test_read_mixed_object(fd):
    obj = ScriptDataObject()

    # Preserves insertion order
    obj["number"] = 123
    obj["string"] = "foobar"
    obj["bool"] = True


    assert ScriptDataObject.read(fd) == obj
    assert fd.tell() == MIXED_VALUES_SIZE



