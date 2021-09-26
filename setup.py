#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          : setup.py
# Author             : Podalirius (@podalirius_)
# Date created       : 25 Sep 2021

import setuptools

long_description = "A Python native library containing lots of useful functions to write efficient scripts to hack stuff."

setuptools.setup(
    name="sectools",
    version="0.0.1",
    description="",
    url="https://github.com/p0dalirius/sectools",
    author="Podalirius",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="podalirius@protonmail.com",
    packages=setuptools.find_packages(),
    license="GPL2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.4",
)