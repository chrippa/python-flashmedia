# vim: set fileencoding=utf8 :

from . import with_fd
from nose.tools import *

from flashmedia.tag import (Tag, VideoData, AVCVideoData,
                            TAG_TYPE_VIDEO, VIDEO_CODEC_ID_AVC,
                            VIDEO_FRAME_TYPE_KEY_FRAME, AVC_PACKET_TYPE_NALU)

VIDEO_DATA = b"\t\x00\x00\x0f\x00\x00{\x00\x00\x00\x00\x17\x01\x00\x00\x00video data\x00\x00\x00\x1a"
VIDEO_DATA_SIZE = len(VIDEO_DATA)

def create_video_tag():
    avc = AVCVideoData(AVC_PACKET_TYPE_NALU, 0, b"video data")
    videodata = VideoData(VIDEO_FRAME_TYPE_KEY_FRAME, VIDEO_CODEC_ID_AVC, avc)
    tag = Tag(TAG_TYPE_VIDEO, 123, videodata)

    return tag


def test_serialize_video_data():
    tag = create_video_tag()

    assert tag.serialize() == VIDEO_DATA

def test_serialize_into_video_data():
    tag = create_video_tag()
    buf = bytearray(tag.size)

    assert tag.serialize_into(buf, 0) == tag.size
    assert buf == VIDEO_DATA

def test_serialize_into_video_data_big_buffer():
    tag = create_video_tag()
    buf = bytearray(tag.size * 2)

    assert tag.serialize_into(buf, 0) == tag.size
    assert buf[:tag.size] == VIDEO_DATA


def test_size_video_data():
    tag = create_video_tag()

    assert tag.size == VIDEO_DATA_SIZE


@with_fd(VIDEO_DATA)
def test_deserialize_video_data(fd):
    tag = Tag.deserialize(fd)

    assert tag.type == TAG_TYPE_VIDEO
    assert tag.timestamp == 123

    assert isinstance(tag.data, VideoData)
    assert tag.data.type == VIDEO_FRAME_TYPE_KEY_FRAME
    assert tag.data.codec == VIDEO_CODEC_ID_AVC

    assert isinstance(tag.data.data, AVCVideoData)
    assert tag.data.data.type == AVC_PACKET_TYPE_NALU
    assert tag.data.data.data == b"video data"

    assert fd.tell() == VIDEO_DATA_SIZE


def test_deserialize_from_video_data():
    buf = VIDEO_DATA * 2
    offset = 0

    tag, offset = Tag.deserialize_from(buf, offset)

    assert tag.type == TAG_TYPE_VIDEO
    assert tag.timestamp == 123

    assert isinstance(tag.data, VideoData)
    assert tag.data.type == VIDEO_FRAME_TYPE_KEY_FRAME
    assert tag.data.codec == VIDEO_CODEC_ID_AVC

    assert isinstance(tag.data.data, AVCVideoData)
    assert tag.data.data.type == AVC_PACKET_TYPE_NALU
    assert tag.data.data.data == b"video data"

    assert offset == VIDEO_DATA_SIZE


