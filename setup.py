#!/usr/bin/env python

from setuptools import setup, find_packages
from sys import version_info

version = "0.1"

setup(name="python-flashmedia",
      version=version,
      description="FLV/F4V parsing and creating library",
      url="https://github.com/chrippa/python-flashmedia",
      author="Christopher Rosell",
      author_email="chrippa@tanuki.se",
      license="Simplified BSD",
      packages=["flashmedia"],
      package_dir={"": "src"}
)
