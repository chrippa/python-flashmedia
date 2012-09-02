python-flv
==========
This is a python library for parsing and modifying FLV files.

Main difference from the already existing flvlib is that it reads data from any python file-like object and does not require the object to support seek (e.g network streams). Tag objects can also be serialized, making it possible to create or modify FLV files.

Currently it has been tested to be compatible with Python 2.7 and 3.2.


Example usage
-------------

```python
# Open the FLV, pass any readable file-like object
try:
    flvobj = flv.FLV(fd)
except flv.FLVError as err:
    print("Invalid FLV")
    sys.exit()

# Iterate over tags
for tag in flvobj:
    # tag.data contains the parsed data, it's either a AudioData, VideoData or ScriptData object
    print("Tag with timestamp %d contains %s" % (tag.timestamp, repr(tag.data)))

    # Modify the metadata
    if isinstance(tag.data, flv.tag.ScriptData) and tag.data.name == "onMetaData":
        tag.data.value["description"] = "This file has been modified through python!"

    # Serialize the tag back into a bytestream
    data = tag.serialize()

```
