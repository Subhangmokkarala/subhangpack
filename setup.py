from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '1.0.1'
DESCRIPTION = 'Youre too early'

# Setting up
setup(
    name="subhangpack",
    version=VERSION,
    author="SubhangMokkarala",
    author_email="<subhangmokkarala@gmail>",
    description=DESCRIPTION,
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
        "Development Status :: Learning",
        "Intended Audience :: Developers",
        "license= MIT",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
