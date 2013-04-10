from . import with_fd
from flashmedia.types import AMF3Integer

MIN = -268435456
MIN_BYTES = b"\xc0\x80\x80\x00"
MIN_SIZE = len(MIN_BYTES)

MAX = 268435455
MAX_BYTES = b"\xbf\xff\xff\xff"
MAX_SIZE = len(MAX_BYTES)

ZERO = 0
ZERO_BYTES = b"\x00"
ZERO_SIZE = len(ZERO_BYTES)

def test_pack_min():
    assert AMF3Integer.pack(MIN) == MIN_BYTES

def test_pack_max():
    assert AMF3Integer.pack(MAX) == MAX_BYTES

def test_pack_zero():
    assert AMF3Integer.pack(ZERO) == ZERO_BYTES


def test_size_min():
    assert AMF3Integer.size(MIN) == MIN_SIZE

def test_size_max():
    assert AMF3Integer.size(MAX) == MAX_SIZE

def test_size_zero():
    assert AMF3Integer.size(ZERO) == ZERO_SIZE


@with_fd(MIN_BYTES)
def test_read_min(fd):
    assert AMF3Integer.read(fd) == MIN


@with_fd(MAX_BYTES)
def test_read_max(fd):
    assert AMF3Integer.read(fd) == MAX

@with_fd(ZERO_BYTES)
def test_read_zero(fd):
    assert AMF3Integer.read(fd) == ZERO
