from distutils.core import setup

import py2exe

setup(
    windows=[{"script": "part_manager.py"}],
    options={"py2exe": {"includes": ["sip"]}}
)