import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "Pypi.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

VERSION = "0.3.5"
DESCRIPTION = "Classes for technical analysis of stocks."

# Setting up
setup(
    name="stock-analyser",
    version=VERSION,
    author="Stefanie Molin",
    author_email="d19cyber@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=required,
    keywords=[
        "python",
        "stock",
        "analysis",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
