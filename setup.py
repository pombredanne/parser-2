#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
	name="DependencyWatcher-Parser",
	version="1.0",
	url="http://github.com/DependencyWatcher/parser/",
	author="Michael Spector",
	license="Apache 2.0",
	author_email="spektom@gmail.com",
	long_description=__doc__,
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		"lxml",
                "pyparsing",
                "scandir"
	]
)
