# vim: set fileencoding=utf8 :

from . import with_fd
from nose.tools import *

from flashmedia.tag import Header

HEADER = b"FLV\x01\x05\x00\x00\x00\t\x00\x00\x00\x00"
HEADER_SIZE = len(HEADER)

def create_header():
    header = Header(has_audio=True, has_video=True)
    return header

def test_serialize():
    header = create_header()

    assert header.serialize() == HEADER

def test_serialize_into():
    header = create_header()
    buf = bytearray(header.size)
    offset = 0

    assert header.serialize_into(buf, offset) == header.size
    assert buf == HEADER


def test_size():
    header = create_header()

    assert header.size == HEADER_SIZE


@with_fd(HEADER)
def test_deserialize(fd):
    header = Header.deserialize(fd)

    assert fd.tell() == HEADER_SIZE
    assert header.has_audio == True
    assert header.has_video == True

def test_deserialize_from():
    buf = HEADER * 2
    offset = 0

    header, offset = Header.deserialize_from(buf, offset)
    assert header.has_audio == True
    assert header.has_video == True

    header, offset = Header.deserialize_from(buf, offset)
    assert header.has_audio == True
    assert header.has_video == True


