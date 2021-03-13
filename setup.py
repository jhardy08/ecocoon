# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in ecocoon/__init__.py
from ecocoon import __version__ as version

setup(
	name='ecocoon',
	version=version,
	description='ensembles de modules pour e-cocoon sprl',
	author='JH',
	author_email='jh@e-cocoon.be',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
