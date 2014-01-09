# -*- coding: utf-8 -*-
from distutils.core import setup

setup (
    name='petra-python-deploy-test',
    version='0.1',
    author='Petra Barus',
    author_email='petra.barus@gmail.com',
    url='http://github.com/petrabarus/python-deploy-test',
    license='BSD licence, see',
    description='Testing deploying executable python application',
    long_description=open('README.md').read(),
    scripts=['scripts/petrabarus-testapp.py'],
    packages=['petrabarus_test'],
    package_dir={'': 'src'}
)