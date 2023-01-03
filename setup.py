import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION = "\n" + fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

VERSION = "0.3.7"
DESCRIPTION = "Classes for technical analysis of stocks."

# Setting up
setup(
    name="stock-analyser",
    version=VERSION,
    author="Stefanie Molin",
    author_email="d19cyber@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/themagicalmammal/stock-analyser",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    install_requires=required,    
    project_urls={
        # "Website": "https://github.com/themagicalmammal/stock-analyser",
        # "Source code": "https://github.com/themagicalmammal/stock-analyser",
        "Documentation":
        "https://github.com/themagicalmammal/stock-analyser/blob/main/README.md",
        "Bug tracker":
        "https://github.com/themagicalmammal/stock-analyser/issues",
    },
    keywords=[
        "python",
        "stock",
        "analysis",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Utilities",
    ],
)
