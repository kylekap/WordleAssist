# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='WordleAssist',
    version='0.0.1',
    description='Basic package',
    long_description=readme,
    author='Kyle Patterson',
    url='https://github.com/kylekap/WorldeAssist',
    license=license,
    packages=find_packages(exclude=('Tests', 'Docs', 'Results'))
)

