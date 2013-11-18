#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :copyright: Copyright 2013 by Hugo Geoffroy
    :contact: hugo@pstch.net
"""


from setuptools import setup


setup(
    name='django-auto-perms',
    version='0.1.0',
    description='Django automatic model permissions',
    long_description="small hack to make URL confs more readable (permissions part)",
    author='Hugo Geoffroy',
    author_email='hugo@pstch.net',
    packages = ['django_auto_perms'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
)
