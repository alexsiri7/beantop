import os
from setuptools import setup

version = '0.2.1'
README = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(README).read() + 'nn'

setup(name='beantop', version=version, 
    author='alexsiri7',
    author_email='alexsiri7@gmail.com',
    license='GPL',
    long_description=long_description,
    url='https://github.com/alexsiri7/beantop', 
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Programming Language :: Python", 
        "Intended Audience :: System Administrators", 
        "Topic :: Utilities"], 
    scripts=['scripts/beantop'],        
    )
