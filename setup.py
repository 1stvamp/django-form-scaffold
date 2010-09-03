"""Installer for django-form-scaffold"""

try:
        from setuptools import setup, find_packages
except ImportError:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages
setup(
        name='django-form-scaffold',
        description='Helper functions for generating templated markup of Django forms',
        version='1.0.1',
        author='Wes Mason',
        author_email='wes[at]1stvamp[dot]org',
        url='http://github.com/1stvamp/django-form-scaffold',
        packages=find_packages(exclude=['ez_setup']),
        setup_requires=(
                'django>=1.1',
        ),
        provides=(
                'dfs',
        ),
        license='Apache License 2.0'
)
