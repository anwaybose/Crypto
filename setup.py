'''
from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup
d = generate_distutils_setup(
    packages=['python_crypto'],
    package_dir={'': 'src'}
)
setup(**d)
'''

#!/usr/bin/env python

from distutils.core import setup

setup(name='Crypto_utils',
      version='1.0',
      description='Pycryptodome',
      author='Anway Bose',
      author_email='anway.bose@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['python_crypto'],
      package_dir={'': 'src'}
     )