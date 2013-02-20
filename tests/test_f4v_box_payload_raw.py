# vim: set fileencoding=utf8 :

from . import with_fd
from nose.tools import *

from flashmedia.box import RawPayload

PAYLOAD = b"some data"
PAYLOAD_SIZE = len(PAYLOAD)

def create_payload():
    payload = RawPayload(b"some data")

    return payload

def test_serialize_payload():
    payload = create_payload()

    assert payload.serialize() == PAYLOAD


def test_size_payload():
    payload = create_payload()

    assert payload.size == PAYLOAD_SIZE


@with_fd(PAYLOAD)
def test_deserialize_paypload(fd):
    payload = RawPayload.deserialize(fd)

    assert payload.data == b"some data"
    assert fd.tell() == PAYLOAD_SIZE

