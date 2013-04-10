from . import with_fd
from flashmedia.types import AMF3String

STR = "String . String"
STR_BYTES = b"\x1fString . String"
STR_BYTES_CACHE = b"\x00"
STR_SIZE = len(STR_BYTES)

def test_pack_str():
    assert AMF3String.pack(STR, []) == STR_BYTES

def test_pack_str_cache():
    cache = []
    assert AMF3String.pack(STR, cache) == STR_BYTES
    assert AMF3String.pack(STR, cache) == STR_BYTES_CACHE

def test_size_str():
    assert AMF3String.size(STR, []) == STR_SIZE


@with_fd(STR_BYTES)
def test_read_str(fd):
    assert AMF3String.read(fd, []) == STR

