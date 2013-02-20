# vim: set fileencoding=utf8 :

from . import with_fd
from flashmedia.types import ScriptDataStrictArray
from nose.tools import *

EMPTY_LIST = b"\x00\x00\x00\x00"
EMPTY_LIST_SIZE = len(EMPTY_LIST)
NUMBERS_LIST = b"\x00\x00\x00\x03\x00?\xf0\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00@\x08\x00\x00\x00\x00\x00\x00"
NUMBERS_LIST_SIZE = len(NUMBERS_LIST)
STRINGS_LIST = b"\x00\x00\x00\x03\x02\x00\x011\x02\x00\x012\x02\x00\x013"
STRINGS_LIST_SIZE = len(STRINGS_LIST)
BOOLEANS_LIST = b"\x00\x00\x00\x03\x01\x01\x01\x00\x01\x01"
BOOLEANS_LIST_SIZE = len(BOOLEANS_LIST)
MIXED_LIST = b"\x00\x00\x00\x03\x00?\xf0\x00\x00\x00\x00\x00\x00\x02\x00\x012\x01\x01"
MIXED_LIST_SIZE = len(MIXED_LIST)


def test_pack_empty_list():
    assert ScriptDataStrictArray([]) == EMPTY_LIST

def test_pack_numbers_list():
    assert ScriptDataStrictArray([1, 2, 3]) == NUMBERS_LIST

def test_pack_strings_list():
    assert ScriptDataStrictArray(["1", "2", "3"]) == STRINGS_LIST

def test_pack_booleans_list():
    assert ScriptDataStrictArray([True, False, True]) == BOOLEANS_LIST

def test_pack_mixed_list():
    assert ScriptDataStrictArray([1, "2", True]) == MIXED_LIST


def test_size_empty_list():
    assert ScriptDataStrictArray.size([]) == EMPTY_LIST_SIZE

def test_size_numbers_list():
    assert ScriptDataStrictArray.size([1, 2, 3]) == NUMBERS_LIST_SIZE

def test_size_strings_list():
    assert ScriptDataStrictArray.size(["1", "2", "3"]) == STRINGS_LIST_SIZE

def test_size_booleans_list():
    assert ScriptDataStrictArray.size([True, False, True]) == BOOLEANS_LIST_SIZE

def test_size_mixed_list():
    assert ScriptDataStrictArray.size([1, "2", True]) == MIXED_LIST_SIZE


@with_fd(EMPTY_LIST)
def test_unpack_empty_list(fd):
    assert ScriptDataStrictArray.read(fd) == []
    assert fd.tell() == EMPTY_LIST_SIZE

@with_fd(NUMBERS_LIST)
def test_unpack_numbers_list(fd):
    assert ScriptDataStrictArray.read(fd) == [1, 2, 3]
    assert fd.tell() == NUMBERS_LIST_SIZE

@with_fd(STRINGS_LIST)
def test_unpack_strings_list(fd):
    assert ScriptDataStrictArray.read(fd) == ["1", "2", "3"]
    assert fd.tell() == STRINGS_LIST_SIZE

@with_fd(BOOLEANS_LIST)
def test_unpack_booleans_list(fd):
    assert ScriptDataStrictArray.read(fd) == [True, False, True]
    assert fd.tell() == BOOLEANS_LIST_SIZE

@with_fd(MIXED_LIST)
def test_unpack_mixed_list(fd):
    assert ScriptDataStrictArray.read(fd) == [1, "2", True]
    assert fd.tell() == MIXED_LIST_SIZE


