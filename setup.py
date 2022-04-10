import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "Pypi.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.3.4"
DESCRIPTION = "Classes for technical analysis of stocks."

# Setting up
setup(
    name="stock-analyser",
    version=VERSION,
    author="Stefanie Molin",
    author_email="d19cyber@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        "matplotlib>=3.0.2",
        "numpy>=1.15.2",
        "pandas>=0.23.4",
        "pandas-datareader>=0.7.0",
        "seaborn>=0.11.0",
        "statsmodels>=0.11.1",
        "mplfinance>=0.12.7a4",
    ],
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
