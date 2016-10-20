# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="data_structures",
    description="Classic data structures.",
    version='0.1.1',
    author="Zach Rickert",
    author_email="zachrickert@gmail.com",
    license='MIT',
    py_modules=['linked_list'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'tox']},
)
