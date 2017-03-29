# -*- coding: utf-8 -*-

from os.path import dirname, join
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from fastread import __version__

with open(join(dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

with open(join(dirname(__file__), 'README.md')) as f:
    long_description = f.read()


class PyTest(TestCommand):
    user_options = []

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, '-m', 'pytest', 'tests'])
        raise SystemExit(errno)

setup(
    name='fastread',
    version=__version__,
    install_requires=required,
    url='https://github.com/stasfilin/fastread',
    license='MIT',
    author='Stanislav Filin (stasfilin)',
    author_email='stasfilinmusic@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    description='',
    long_description=long_description,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',

    ],
    cmdclass=dict(test=PyTest)
)
