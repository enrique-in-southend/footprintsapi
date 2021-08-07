"""Required setup file."""
import re
from pathlib import Path

from setuptools import find_packages, setup

ROOT_DIR = Path().resolve(strict=True)

# Get version number
with open("footprintsapi/__init__.py", "r") as fd:
    VERSION = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)

if not VERSION:
    raise RuntimeError("Cannot find version information.")

# Get the readme
with open(ROOT_DIR / "README.md") as readme:
    long_description = readme.read()


setup(
    name="footprintsapi",
    version=VERSION,
    description="API wrapper for the BMC (Numara) Footprints SOAP API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jesus-E-Rodriguez/footprintsapi.git",
    author="Jesus Rodriguez",
    author_email="jesus_enrique@rocketmail.com",
    license="MIT License",
    packages=find_packages(),
    install_requires=["zeep~=4.0.0", "requests~=2.26.0"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
)
