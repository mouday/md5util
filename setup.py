# -*- coding: utf-8 -*-

# @Date    : 2019-12-20
# @Author  : Peng Shiyu

from setuptools import setup, find_packages

"""
打包的用的setup必须引入，
"""

VERSION = '0.0.3'

setup(
    name='md5util',
    version=VERSION,
    description="a quick md5 tool",
    long_description='a quick md5 tool just like php',
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='md5util',
    author='Peng Shiyu',
    author_email='pengshiyuyx@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[]
)
