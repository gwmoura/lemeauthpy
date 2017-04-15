import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))



PACKAGE = "lemeauth"
NAME = "lemeauth"
DESCRIPTION = "Package to use Leme API to authenticate"
AUTHOR = "George Moura"
AUTHOR_EMAIL = "gwmoura@gcodetec.com"
URL = "github.com/lememilitar/lemeauthpy"
VERSION = __import__(PACKAGE).__version__

install_requires = ['requests']

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django, Flask",
    ],
    zip_safe=False,
)
