#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

# setup_requirements = ['pytest-runner', ]

# test_requirements = ['pytest>=3', ]

setup(
    author="Takuya Kodama",
    author_email='lukefone.story@gmail.com',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    description="attemption of create python package",
    entry_points={
        'console_scripts': [
            'tkpie=tkpie.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='tkpie',
    name='tkpie',
    pymodule=['tkpie/tkpie'],
    packages=find_packages(include=['tkpie', 'tkpie.*']),
    # setup_requires=setup_requirements,
    test_suite='tests',
    # tests_require=test_requirements,
    url='https://github.com/takuya0412/tkpie',
    version='0.1.0',
    zip_safe=False,
)
