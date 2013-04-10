from . import with_fd
from flashmedia.types import AMF3Date, AMF3DatePacker

DATE = AMF3Date(0)
DATE_BYTES = b"\x01\x00\x00\x00\x00\x00\x00\x00\x00"
DATE_SIZE = len(DATE_BYTES)

def test_pack_date():
    assert AMF3DatePacker.pack(DATE, []) == DATE_BYTES


def test_size_date():
    assert AMF3DatePacker.size(DATE, []) == DATE_SIZE


@with_fd(DATE_BYTES)
def test_read_date(fd):
    val = AMF3DatePacker.read(fd, [])

    assert val.time == DATE.time
