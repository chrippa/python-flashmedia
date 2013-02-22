# vim: set fileencoding=utf8 :

from __future__ import unicode_literals

from . import with_fd
from flashmedia.types import CString


ASCII = b"ABC\x00"
ASCII_SIZE = len(ASCII)

UTF8 = b"\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e\x00"
UTF8_SIZE = len(UTF8)

BROKEN_UTF8 = b"\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x00"
BROKEN_UTF8_SIZE = len(BROKEN_UTF8)


def test_pack_ascii():
    assert CString("ABC", "ascii") == ASCII

def test_pack_utf8():
    assert CString("日本語") == UTF8

def test_pack_into():
    size = ASCII_SIZE + UTF8_SIZE
    buf = bytearray(size)
    offset = 0

    offset = CString.pack_into(buf, offset, "ABC", "ascii")
    offset = CString.pack_into(buf, offset, "日本語")

    assert buf == (ASCII + UTF8)
    assert offset == size


def test_size_ascii():
    assert CString.size("ABC", "ascii") == ASCII_SIZE

def test_size_utf8():
    assert CString.size("日本語") == UTF8_SIZE


@with_fd(ASCII)
def test_read_ascii(fd):
    assert CString.read(fd, "ascii") == "ABC"
    assert fd.tell() == ASCII_SIZE

@with_fd(UTF8)
def test_read_utf8(fd):
    assert CString.read(fd) == "日本語"
    assert fd.tell() == UTF8_SIZE

@with_fd(BROKEN_UTF8)
def test_read_broken_utf8(fd):
    assert CString.read(fd) == "日本"
    assert fd.tell() == BROKEN_UTF8_SIZE

def test_unpack_from():
    buf = ASCII + UTF8 + BROKEN_UTF8

    offset = 0

    val, offset = CString.unpack_from(buf, offset)
    assert val == "ABC"

    val, offset = CString.unpack_from(buf, offset)
    assert val == "日本語"

    val, offset = CString.unpack_from(buf, offset)
    assert val == "日本"


