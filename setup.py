from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '1.0.13'
DESCRIPTION = 'Youre too early'

# Setting up
setup(
    name="subhangpack",
    version=VERSION,
    author="SubhangMokkarala",
    author_email="subhangmokkarala@gmail.com",
    description=DESCRIPTION,
    long_description= open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'tensorflow'],
    entry_points={
        'console_scripts': [
            'subhangpack-hello = subhangpack:hello',
            'subhangpack-devicename = subhangpack:namegen'
        ]
    },
    keywords=['python', 'name', 'generator', 'device', 'random', 'fun', 'subhangpack', 'subhang', 'mokkarala', 'subhangmokkarala'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
