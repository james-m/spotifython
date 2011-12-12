#!/usr/bin/python
#
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

LIB_SPOT_EXT = Extension(
    'spotify',
    ['libspotify.pyx'],
    libraries = ['spotify'],
    )

setup(
    cmdclass = {
        'build_ext': build_ext,
        },
    ext_modules = [
        LIB_SPOT_EXT,
        ],
)
