#!/usr/bin/env python

from distutils.core import setup

setup(
    name='py-noembed',
    version='0.2',
    description='Python Wrapper over NoEmbed',
    author='Jacob Haslehurst',
    author_email='jacob@haslehurst.net',
    url='https://github.com/gizmag/py-noembed',
    packages=['noembed'],
    install_requires=['requests']
)
