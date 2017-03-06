# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='implotcontroler',
    version='0.1.0',
    description='Driver for 2D implot',
    long_description=readme,
    author='Mohammed-Amine Hilaly',
    author_email='Impcreativity@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

