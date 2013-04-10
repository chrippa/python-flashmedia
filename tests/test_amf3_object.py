from . import with_fd
from flashmedia.types import AMF3Object, AMF3ObjectBase, AMF3ObjectPacker

@AMF3ObjectBase.register("org.amf.ASClass")
class ASClass(AMF3ObjectBase):
    def __init__(self, foo, baz=None):
        self.foo = foo
        self.baz = baz


NAMED_TYPE = ASClass("bar")
NAMED_TYPE_BYTES = b"#\x1forg.amf.ASClass\x07baz\x07foo\x01\x06\x07bar"
NAMED_TYPE_SIZE = len(NAMED_TYPE_BYTES)

ANONYMOUS = AMF3Object()
ANONYMOUS["answer"] = 42
ANONYMOUS["foo"] = "bar"
ANONYMOUS_BYTES = b"\x0b\x01\ranswer\x04*\x07foo\x06\x07bar\x01"
ANONYMOUS_SIZE = len(ANONYMOUS_BYTES)

def test_pack_named_type():
    assert AMF3ObjectPacker.pack(NAMED_TYPE, [], [], []) == NAMED_TYPE_BYTES

def test_pack_anonymous():
    assert AMF3ObjectPacker.pack(ANONYMOUS, [], [], []) == ANONYMOUS_BYTES


def test_size_named_type():
    assert AMF3ObjectPacker.size(NAMED_TYPE, [], [], []) == NAMED_TYPE_SIZE

def test_size_anonymous():
    assert AMF3ObjectPacker.size(ANONYMOUS, [], [], []) == ANONYMOUS_SIZE


@with_fd(NAMED_TYPE_BYTES)
def test_read_named_type(fd):
    val = AMF3ObjectPacker.read(fd, [], [], [])

    assert val.foo == NAMED_TYPE.foo
    assert val.baz == NAMED_TYPE.baz

@with_fd(ANONYMOUS_BYTES)
def test_read_anonymous(fd):
    val = AMF3ObjectPacker.read(fd, [], [], [])

    assert val == ANONYMOUS
