"""Installer for django-form-scaffold"""

from setuptools import setup, find_packages

setup(
    name='django-form-scaffold',
    description='Helper functions for generating templated markup of Django forms',
    version='1.1.0',
    author='Wes Mason',
    author_email='wes[at]1stvamp[dot]org',
    url='http://github.com/1stvamp/django-form-scaffold',
    packages=find_packages(),
    license='Apache License 2.0',
    classifiers=(
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ),
    zip_safe=False,
)
