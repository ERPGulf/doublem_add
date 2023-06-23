from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in doublem_add/__init__.py
from doublem_add import __version__ as version

setup(
	name="doublem_add",
	version=version,
	description="This is addon for doublem- which published already",
	author="ERPGulf",
	author_email="support@ERPGulf.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
