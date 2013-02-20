from flashmedia.types import U24LE, S24LE
from nose.tools import *

import struct


""" Unsigned 24-bit Integer (Pack) """

def test_pack_unsigned_min():
    assert U24LE(0) == b"\x00\x00\x00"

def test_pack_unsigned_max():
    assert U24LE(16777215) == b"\xff\xff\xff"

@raises(struct.error)
def test_pack_unsigned_overflow():
    U24LE(16777216)

@raises(struct.error)
def test_pack_unsigned_underflow():
    U24LE(-1)


""" Unsigned 24-bit Integer (Unpack) """

def test_unpack_unsigned_min():
    assert U24LE.unpack(b"\x00\x00\x00")[0] == 0

def test_unpack_unsigned_max():
    assert U24LE.unpack(b"\xff\xff\xff")[0] == 16777215




""" Signed 24-bit Integer (Pack) """

def test_pack_signed_min():
    assert S24LE(-8388608) == b"\x00\x00\x80"

def test_pack_signed_max():
    assert S24LE(8388607) == b"\xff\xff\x7f"

@raises(struct.error)
def test_pack_signed_overflow():
    S24LE(8388608)

@raises(struct.error)
def test_pack_signed_underflow():
    S24LE(-8388609)


""" Signed 24-bit Integer (Unpack) """

def test_unpack_signed_min():
    assert S24LE.unpack(b"\x00\x00\x80")[0] == -8388608

def test_unpack_unsigned_max():
    assert S24LE.unpack(b"\xff\xff\x7f")[0] == 8388607


