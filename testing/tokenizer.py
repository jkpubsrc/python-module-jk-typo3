#!/usr/bin/python3




import re
import os
import sys





from jk_utils import TypedValue
from jk_utils.tokenizer import Token
import jk_php_tokenizer












TYPO3FILEPATH = "test_typo3_LocalConfiguration.php"



tokenizer = jk_php_tokenizer.PHPTokenizer()
with open(TYPO3FILEPATH, "r") as f:
	for token in tokenizer.tokenize(f.read()):
		print(token)
















