#!/usr/bin/env python

from setuptools import setup, find_packages
from sys import version_info

version = "1.0"

setup(name="python-flv",
      version=version,
      description="FLV parsing and creating library",
      url="https://github.com/chrippa/python-flv",
      author="Christopher Rosell",
      author_email="chrippa@tanuki.se",
      license="GPL",
      packages=["flv"],
      package_dir={"": "src"}
)
