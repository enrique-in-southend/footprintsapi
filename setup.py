"""Required setup file."""

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)
from setuptools import find_packages, setup
import re
import os

# Get version number
with open("footprintsapi/__init__.py", "r") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError("Cannot find version information.")

# Get the readme
with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    long_description = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="footprintsapi",
    version=version,
    description="API wrapper for the BMC (Numara) Footprints SOAP API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jesus-E-Rodriguez/footprintsapi.git",
    author="Jesus Rodriguez",
    author_email="jesus_enrique@rocketmail.com",
    license="MIT License",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "appdirs~=1.4.3",
        "attrs~=19.1.0",
        "cached-property~=1.5.1",
        "certifi~=2019.3.9",
        "chardet~=3.0.4",
        "defusedxml~=0.6.0",
        "idna~=2.8",
        "isodate~=0.6.0",
        "lxml~=4.3.3",
        "pytz~=2019.1",
        "requests~=2.21.0",
        "requests-toolbelt~=0.9.1",
        "six~=1.12.0",
        "urllib3~=1.24.3",
        "zeep~=3.3.1",
    ],
    extras_requires={
        "local": [
            "pep8~=1.7.1",
            "pydocstyle~=3.0.0",
            "snowballstemmer~=1.2.1",
            "black~=19.3b0",
            "click~=7.0",
            "toml~=0.10.0",
        ],
        "test": ["coverage~=4.5.3", "requests-mock~=1.6.0"],
    },
    zip_safe=False,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
)
