# -*- coding: utf-8 -*-

import shutil
import sys
import setuptools
import os


## Move previous dist to older folder
source_dir = 'pkg/dist/latest/'
target_dir = 'pkg/dist/older/'
    
file_names = os.listdir(source_dir)
    
for file_name in file_names:
    shutil.move(os.path.join(source_dir, file_name), target_dir)


## Read description from readme
with open("README.md", "r") as fh:
    long_description = fh.read()


## Build setuptools
setuptools.setup(
    name="PySimpleFrame",
    version="1.0.2",
    author="Miguel Silva",
    author_email="miguasjpsilva@gmail.com",
    description="",
    long_description=long_description,
    url="https://github.com/OriDevTeam/PySimpleFrame",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)

## Remove build
## TODO: Move this to setup.cfg if possible
shutil.rmtree('build')
