#!/usr/bin/python3




import re
import os
import sys





import jk_typo3










TYPO3FILEPATH = "test_typo3_LocalConfiguration.php"


parser = jk_typo3.Typo3ConfigurationFileParser()
x = parser.parseFile(TYPO3FILEPATH)

print(x)















