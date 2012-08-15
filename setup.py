#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
VERSION = '1.0.0'

setup(
    name = "django-colorfield",
    version = VERSION,
    description = "A small app providing a colorpicker field for django.",
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
)

