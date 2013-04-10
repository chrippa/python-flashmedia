from . import with_fd
from flashmedia.types import AMF3Array, AMF3ArrayPacker

EMPTY = AMF3Array()
EMPTY_BYTES = b"\x01\x01"
EMPTY_SIZE = len(EMPTY_BYTES)

PRIMITIVE = AMF3Array([1, 2, 3, 4, 5])
PRIMITIVE_BYTES = b"\x0b\x01\x04\x01\x04\x02\x04\x03\x04\x04\x04\x05"
PRIMITIVE_SIZE = len(PRIMITIVE_BYTES)

ASSOCIATIVE = AMF3Array()
ASSOCIATIVE["asdf"] = "fdsa"
ASSOCIATIVE["foo"] = "bar"
ASSOCIATIVE["42"] = "bar"
ASSOCIATIVE[0] = "bar1"
ASSOCIATIVE[1] = "bar2"
ASSOCIATIVE[2] = "bar3"

ASSOCIATIVE_BYTES = b"\x07\tasdf\x06\tfdsa\x07foo\x06\x07bar\x0542\x06\x06\x01\x06\tbar1\x06\tbar2\x06\tbar3"
ASSOCIATIVE_SIZE = len(ASSOCIATIVE_BYTES)

def test_pack_empty():
    assert AMF3ArrayPacker.pack(EMPTY, [], [], []) == EMPTY_BYTES

def test_pack_primitive():
    assert AMF3ArrayPacker.pack(PRIMITIVE, [], [], []) == PRIMITIVE_BYTES

def test_pack_associative():
    assert AMF3ArrayPacker.pack(ASSOCIATIVE, [], [], []) == ASSOCIATIVE_BYTES

def test_size_empty():
    assert AMF3ArrayPacker.size(EMPTY, [], [], []) == EMPTY_SIZE

def test_size_primitive():
    assert AMF3ArrayPacker.size(PRIMITIVE, [], [], []) == PRIMITIVE_SIZE

def test_size_associative():
    assert AMF3ArrayPacker.size(ASSOCIATIVE, [], [], []) == ASSOCIATIVE_SIZE

@with_fd(EMPTY_BYTES)
def test_read_empty(fd):
    assert AMF3ArrayPacker.read(fd, [], [], []) == EMPTY

@with_fd(PRIMITIVE_BYTES)
def test_read_primitive(fd):
    assert AMF3ArrayPacker.read(fd, [], [], []) == PRIMITIVE

@with_fd(ASSOCIATIVE_BYTES)
def test_read_associative(fd):
    assert AMF3ArrayPacker.read(fd, [], [], []) == ASSOCIATIVE

