# vim: set fileencoding=utf8 :

from . import with_fd
from nose.tools import *

from flashmedia.types import ScriptDataString

ASCII = b"\x00\x03ABC"
ASCII_SIZE = len(ASCII)

UTF8 = b"\x00\t\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e"
UTF8_SIZE = len(UTF8)

BROKEN_UTF8 = b"\x00\x08\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa"
BROKEN_UTF8_SIZE = len(BROKEN_UTF8)

def test_pack_ascii():
    assert ScriptDataString("ABC", "ascii") == ASCII

def test_pack_utf8():
    assert ScriptDataString(u"日本語") == UTF8

def test_pack_into():
    size = ASCII_SIZE + UTF8_SIZE
    buf = bytearray(size)
    offset = 0

    offset = ScriptDataString.pack_into(buf, offset, "ABC", "ascii")
    offset = ScriptDataString.pack_into(buf, offset, u"日本語")

    assert buf == (ASCII + UTF8)
    assert offset == size


def test_size_ascii():
    assert ScriptDataString.size("ABC", "ascii") == ASCII_SIZE

def test_size_utf8():
    assert ScriptDataString.size(u"日本語") == UTF8_SIZE


@with_fd(ASCII)
def test_read_ascii(fd):
    assert ScriptDataString.read(fd, "ascii") == "ABC"
    assert fd.tell() == ASCII_SIZE

@with_fd(UTF8)
def test_read_utf8(fd):
    assert ScriptDataString.read(fd) == u"日本語"
    assert fd.tell() == UTF8_SIZE

@with_fd(BROKEN_UTF8)
def test_read_broken_utf8(fd):
    assert ScriptDataString.read(fd) == u"日本"
    assert fd.tell() == BROKEN_UTF8_SIZE

def test_unpack_from():
    buf = ASCII + UTF8 + BROKEN_UTF8
    offset = 0

    val, offset = ScriptDataString.unpack_from(buf, offset)
    assert val == u"ABC"

    val, offset = ScriptDataString.unpack_from(buf, offset)
    assert val == u"日本語"

    val, offset = ScriptDataString.unpack_from(buf, offset)
    assert val == u"日本"


