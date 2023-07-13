from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in techfinite/__init__.py
from techfinite import __version__ as version

setup(
	name="techfinite",
	version=version,
	description="techfinite systems app",
	author="techfinite",
	author_email="tharun.m@techfinite.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
