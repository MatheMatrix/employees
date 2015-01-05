#!/usr/bin/env python

PROJECT = 'employee'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Simple employee system for course design',
    long_description=long_description,

    author='Wei Wang',
    author_email='wei.w@outlook.com',

    url='https://github.com/mathematrix/employee',
    download_url='https://github.com/mathematrix/employee/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.2',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['cliff'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'employee = employee.main:main'
        ],
        'employee.manager': [
            'add = employee.add:Add',
            'summary = employee.summary:Summary',
            'detail = employee.detail:Detail',
            'update = employee.update:Update',
            'delete = employee.delete:Delete',
            'query = employee.query:Query',
            'sort = employee.sort:Sort',
        ],
    },

    zip_safe=False,
)
