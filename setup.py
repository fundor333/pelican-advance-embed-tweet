#!/usr/bin/env python

from codecs import open

from setuptools import setup, find_packages

from pelican_advance_embed_tweet import __version__

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name="pelican_advance_embed_tweet",
    packages=find_packages(
        exclude=['tests', 'docs']
    ),
    short_description="Pelican Plugin for adding tweet into your blog",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    version=__version__,
    license='MIT',
    insert_requires=['pelican'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ], install_requires=['pelican']
)
