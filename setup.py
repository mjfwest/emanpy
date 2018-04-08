#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# ==========================================================================
# Copyright (C) 2016 Dr. Alejandro Pina Ortega
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==========================================================================

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='emanpy',
      version='0.1',
      description='Electric Machine Analysis with Python',
      long_description=readme(),
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
      ],
      keywords='motor generator',
      url='http://github.com/ajpina/emanpy',
      author='Alejandro Pina Ortega',
      author_email='a.pina-ortega@ieee.org',
      license='Apache',
      packages=['emanpy'],
      install_requires=[
          'numpy',
#          'uffema',
#          'logging',
      ],
      include_package_data=True,
      zip_safe=False)