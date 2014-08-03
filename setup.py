from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6',]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='LuckyGo',
      version='1.0',
      description='Lucky go App',
      author='Maxim Popkov, Pavel Timonin, Ledovski Maxim',
      author_email='dales3d@gmail.com',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
)

