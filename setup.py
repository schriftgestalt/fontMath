#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
import sys

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_wheel = {'bdist_wheel'}.intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

# with open('README.rst', 'r') as f:
#     long_description = f.read()

setup(
    name="fontMath",
    version="0.5.2.dev0",
    description="A set of objects for performing math operations on font data.",
    # long_description=long_description,
    author="Tal Leming",
    author_email="tal@typesupply.com",
    url="https://github.com/robotools/fontMath",
    license="MIT",
    package_dir={"": "Lib"},
    packages=find_packages("Lib"),
    test_suite="fontMath",
    setup_requires=pytest_runner + wheel,
    tests_require=[
        'pytest>=3.0.3',
    ],
    install_requires=[
        "fonttools>=3.32.0",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Editors :: Vector-Based',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
