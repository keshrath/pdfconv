# -*- coding: utf-8 -*-

######################################################################################
# 
#    Copyright (C) 2017 Mathias Markl
#
#    This program is free software; you can redistribute it and/or
#    modify it under the terms of the GNU General Public License
#    as published by the Free Software Foundation; either version 2
#    of the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#######################################################################################

"""
PDF Converter

See:
https://github.com/keshrath/pdfconv
"""

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pdfconv",
    version = "1.0.11",
    author = "Mathias Markl",
    author_email = "mathias.markl@mukit.at",
    description = "PDF Converter",
    license = "GPLv2",
    keywords = "converter pdf library",
    url = "https://github.com/keshrath/pdfconv",
    packages = find_packages(exclude=['contrib', 'docs', 'tests']),
    long_description = read('README.rst'),
    platforms = [
        'any'
    ],
    classifiers = [
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    extras_require = {
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
