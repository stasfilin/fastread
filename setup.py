# -*- coding: utf-8 -*-

from os.path import dirname, join
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from fastread import __version__

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()


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
    install_requires=[],
    url='https://github.com/stasfilin/fastread',
    license='Apache Software License',
    author='Stanislav Filin (stasfilin)',
    author_email='stasfilinmusic@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    description='',
    long_description=LONG_DESCRIPTION,
    extras_require={
        'performance':  ['pytest==3.0.3',
                         'pep8==1.7.0',
                         'pyflakes==1.3.0',
                         'coverage==4.2',
                         'pytest-cov==2.4.0']
    },
    download_url='https://github.com/stasfilin/fastread/tarball/v0.0.2',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
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
