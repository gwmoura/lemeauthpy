PACKAGE = "lemeauth"
NAME = "Leme Auth"
DESCRIPTION = "Package to use Leme API to authenticate"
AUTHOR = "George Moura"
AUTHOR_EMAIL = "gwmoura@gcodetec.com"
URL = "github.com/lememilitar/lemeauthpy"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.rst"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    package_data=find_package_data(
   PACKAGE,
   only_in_packages=False
   ),
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
