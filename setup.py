#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
VERSION = '0.1.0'

setup(
    name = "django-colorfield",
    version = VERSION,
    url = 'https://github.com/ekaputra07/django-colorfield',
	download_url = 'https://github.com/ekaputra07/django-colorfield/downloads',
    description = "A small app providing a colorpicker field for django.",
    author = 'Eka Putra (original version: https://github.com/jabapyth/django-colorfield)',
    author_email = 'ekaputra@balitechy.com',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
)

