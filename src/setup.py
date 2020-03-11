################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 4 - Beta",
		"License :: OSI Approved :: Apache Software License",
	],
	description = "This module provides functions and classes to assist in working with Typo3 installations.",
	download_url = "https://github.com/jkpubsrc/python-module-jk-typo3/tarball/0.2020.3.11",
	include_package_data = False,
	install_requires = [
		"jk_utils",
		"jk_typing",
		"jk_json",
		"jk_version",
		"jk_php_tokenizer",
	],
	keywords = [
		"typo3",
		"php",
	],
	license = "Apache 2.0",
	name = "jk_typo3",
	packages = [
		"jk_typo3",
	],
	url = "https://github.com/jkpubsrc/python-module-jk-typo3",
	version = "0.2020.3.11",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
