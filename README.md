# subhangpack
hello
namegen

[![Python Package](https://github.com/Subhangmokkarala/subhangpack/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Subhangmokkarala/subhangpack/actions/workflows/python-publish.yml)

## to install
```bash
pip install subhangpack
```
## to use
```python
from subhangpack import namegen
```
## to generate a random name
```python
namegen.gen()
```
## to generate from terminal
```bash
subhangpack-devicename
```

# pip package for generating random names for homelab and network devices

# noobs guide for making a pip package

### 0. Install pip
```bash
sudo apt install python3-pip
```
### install libraries
```bash 
pip install wheel
pip install setuptools
```
### 1. Make a new folder and cd into it which will be the name of your package
```bash
mkdir yourpackagename
cd yourpackagename
```
### 2. Make a init.py file in the folder 
```bash
touch __init__.py
```
### 3. Make a py file which will be the main file of your package to say what your package does
```bash
touch namegen.py
```
### 4. add your module code in the py file to make it work
```python   
#write your code here
```
### 5. import your module in the init.py file to say that it is a package 
```python
from .namegen import *
```
### 6. Make a setup.py file
```bash
touch setup.py
```
### 7. Add the following code in the setup.py file
```python
from setuptools import setup

setup(name='yourpackagename',
      version='0.1',
      description='write a description here',
      url='
        author='your name',
        author_email='your email',
        license='MIT',
        packages=['yourpackagename'],
        zip_safe=False)
```
### 8. now package your module for source distribution
```bash
python setup.py sdist
```
### 9. now use wheel to package your module for build distribution
```bash
python setup.py bdist_wheel
```
### 10. now install your module to test it locally before publishing it to pypi
```bash
pip install yourpackagename.whl
```
### 11. now you can use your module in any python file
```python
import yourpackagename
```
### 12. now you can upload your module to pypi
```bash
pip install twine
```
### 13. now upload your module to pypi
```bash
twine upload dist/*
```
### 14. now you can install your module from pypi
```bash
pip install yourpackagename
```

# tada you have made your first pip package

