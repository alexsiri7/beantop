import os
from setuptools import setup, find_packages


version = '0.2.4'
README = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(README).read() + 'nn'

setup(name='beantop', version=version, 
    author='alexsiri7',
    author_email='alexsiri7@gmail.com',
    license='GPL',
    long_description=long_description,
    url='https://github.com/alexsiri7/beantop', 
    packages = find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Programming Language :: Python", 
        "Intended Audience :: System Administrators", 
        "Topic :: Utilities"], 
    test_suite = "beantop.tests",
    entry_points = {
     'console_scripts': [
         'beantop = beantop.beantop:main',
         ],
      },

    )
