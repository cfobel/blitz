#!/usr/bin/env python

from distutils.core import setup

setup(name = "blitz",
    version = "0.0.1",
    description = ("Blitz++ headers as Python package to make it easy to "
                   "install"),
    keywords = "Blitz++ blitz",
    author = "Christian Fobel",
    url = "https://github.com/cfobel/blitz",
    license = "GPL",
    long_description = """""",
    packages = ['blitz'],

    package_data={'blitz': ['include/*.*', 'include/blitz/*.*',
                            'lib/*.*', 'cython_include/*.*']}
)
