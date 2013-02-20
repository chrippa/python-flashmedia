from flashmedia.types import U24BE, S24BE
from nose.tools import raises

import struct


""" Unsigned 24-bit Integer (Pack) """

def test_pack_unsigned_min():
    assert U24BE(0) == b"\x00\x00\x00"

def test_pack_unsigned_max():
    assert U24BE(16777215) == b"\xff\xff\xff"

@raises(struct.error)
def test_pack_unsigned_overflow():
    U24BE(16777216)

@raises(struct.error)
def test_pack_unsigned_underflow():
    U24BE(-1)


""" Unsigned 24-bit Integer (Unpack) """

def test_unpack_unsigned_min():
    assert U24BE.unpack(b"\x00\x00\x00")[0] == 0

def test_unpack_unsigned_max():
    assert U24BE.unpack(b"\xff\xff\xff")[0] == 16777215




""" Signed 24-bit Integer (Pack) """

def test_pack_signed_min():
    assert S24BE(-8388608) == b"\x80\x00\x00"

def test_pack_signed_max():
    assert S24BE(8388607) == b"\x7f\xff\xff"

@raises(struct.error)
def test_pack_signed_overflow():
    S24BE(8388608)

@raises(struct.error)
def test_pack_signed_underflow():
    S24BE(-8388609)


""" Signed 24-bit Integer (Unpack) """

def test_unpack_signed_min():
    assert S24BE.unpack(b"\x80\x00\x00")[0] == -8388608

def test_unpack_signed_max():
    assert S24BE.unpack(b"\x7f\xff\xff")[0] == 8388607


