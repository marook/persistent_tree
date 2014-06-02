#!/usr/bin/python2
# -*- coding: utf-8 -*-

from distutils import core
from glob import glob
import os
from os import path
import sys

class Test(core.Command):

    user_options = []

    def initialize_options(self):
        self._dir = os.getcwd()

    def finalize_options(self):
        pass

    def run(self):
        import unittest

        sys.path.insert(0, 'src')

        testfiles = [ ]
        for t in glob(path.join(self._dir, 'src', 'test_*.py')):
            if not t.endswith('__init__.py'):
                testfiles.append('.'.join(
                    [path.splitext(path.basename(t))[0]])
                )

        tests = unittest.TestLoader().loadTestsFromNames(testfiles)
        t = unittest.TextTestRunner(verbosity = 1)
        t.run(tests)

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
    cmdclass = {'test': Test},
)
