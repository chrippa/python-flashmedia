python-flashmedia
==========
This is a Python library for parsing and modifying various formats related to Adobe Flash.
A main goal of the project is to be lossless, so that it is possible to deserialize the data and the serialize it back again without losing any data.
Currently it aims to be compatible with Python 2.6, 2.7 and 3.2+.


Example usage
-------------

```python

from flashmedia import FLV, FLVError
from flashmedia.tag import ScriptData

# Open a FLV, pass any readable file-like object
try:
    flv = FLV(fd)
except FLVError as err:
    print("Invalid FLV")
    sys.exit()

# Iterate over tags
for tag in flv:
    # tag.data contains the parsed data, it's either a AudioData, VideoData or ScriptData object
    print("Tag with timestamp %d contains %s" % (tag.timestamp, repr(tag.data)))

    # Modify the metadata
    if isinstance(tag.data, ScriptData) and tag.data.name == "onMetaData":
        tag.data.value["description"] = "This file has been modified through python!"

    # Serialize the tag back into bytes
    data = tag.serialize()

```
