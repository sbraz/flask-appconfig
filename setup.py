#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='flask-appconfig',
    version='0.1dev',
    description=('Configures Flask applications from the environment '
                 '(Heroku) et. al. Also aims to standardize configuration.'),
    long_description=read('README.rst'),
    author='Marc Brinkmann',
    author_email='git@marcbrinkmann.de',
    url='http://github.com/mbr/flask-appconfig',
    license='MIT',
    packages=find_packages(exclude=['test']),
    install_requires=['flask'],
)