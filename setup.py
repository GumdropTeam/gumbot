#!/usr/bin/env python

import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="gumbot",
        version="0.0.1",
        packages=setuptools.find_packages(),
        install_requires=[
            "ahk==1.8.1"
        ]
    )