#!/usr/bin/python2
# -*- coding: utf-8 -*-

from distutils import core
from os import path

core.setup(
    name = 'persistent_tree',
    version = '0.0.1',
    description = '',
    long_description = '',
    author = 'Markus Peröbner',
    author_email = 'markus.peroebner@gmail.com',
    data_files = [
        (path.join('share', 'doc', 'persistent_tree'), ['README'])
    ],
    packages = ['persistent_tree',],
    package_dir = {'': 'src'},
)
