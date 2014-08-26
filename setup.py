#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'dotenv'
]

test_requirements = [
    'dotenv'
]

setup(
    name='fbopen',
    version='0.0.1',
    description='Python access to the FBOpen API',
    long_description=readme + '\n\n' + history,
    author='Alan deLevie',
    author_email='alan.delevie@gsa.gov',
    url='https://github.com/18f/fbopen-python',
    packages=[
        'fbopen',
    ],
    package_dir={'fbopen':
                 'fbopen'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='fbopen',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
