from setuptools import setup
import os
import sys

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(name='gplaycli2',
		version='3.30',
		description='GPlayCli2, a Google play downloader command line interface',
		long_description=long_description,
		long_description_content_type="text/markdown",
		author="besendorf",
		author_email="janik@besendorf.org",
		url="https://github.com/besendorf/gplaycli",
		license="AGPLv3",
		entry_points={
			'console_scripts': [
				'gplaycli = gplaycli2.gplaycli:main',
			],
		},
		packages=[
			'gplaycli2',
		],
		package_dir={
			'gplaycli2': 'gplaycli2',
		},
		data_files=[
			['etc/gplaycli', ['gplaycli.conf']],
		],
		install_requires=[
				'gpapi2>=0.4.4.4',
				'pyaxmlparser',
		],
)
