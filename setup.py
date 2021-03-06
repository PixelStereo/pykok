#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import versioneer
import os, sys
sys.path.append(os.path.abspath('./pykok'))
from _version import get_versions
__version__ = get_versions()['version']
del get_versions
__version__ = __version__.split('+')
__version__ = __version__[0]

setup(
  name = 'pykok',
  packages = ['pykok'],
  version=versioneer.get_version(),
  cmdclass=versioneer.get_cmdclass(),
  description = 'a lightweight API to make inventory applications',
  author = 'Pixel Stereo',
  url='https://github.com/PixelStereo/pykok',
  download_url = 'https://github.com/PixelStereo/pykok/tarball/' + __version__,
  classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
