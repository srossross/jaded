'''
@author: sean
'''

from setuptools import setup, find_packages

setup(
    name='Jaded',
    version="dev",
    author='Sean Ross-Ross',
    author_email='sean.ross-ross@continuum.io',
    url='',
    packages=find_packages(),
    entry_points={
          'console_scripts': [
              'jaded = jaded.scripts.cli:main',
              ]
                 },

)

