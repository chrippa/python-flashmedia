# vim: set fileencoding=utf8 :

from . import with_fd
from nose.tools import *

from flashmedia.box import Box, BoxPayloadMDAT

BOX = b"\x00\x00\x00\x11mdatsome data"
BOX_SIZE = len(BOX)

def create_box():
    payload = BoxPayloadMDAT(b"some data")
    box = Box("mdat", payload)

    return box

def test_serialize_box():
    box = create_box()

    assert box.serialize() == BOX


def test_size_box():
    box = create_box()

    assert box.size == BOX_SIZE


@with_fd(BOX)
def test_deserialize_paypload(fd):
    box = Box.deserialize(fd)

    assert isinstance(box.payload, BoxPayloadMDAT)
    assert box.payload.data == b"some data"
    assert fd.tell() == BOX_SIZE

