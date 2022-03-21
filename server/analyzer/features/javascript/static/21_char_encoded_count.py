# from config import JS_RESERVED_WORDS_PATH
import re

import esprima
from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.datatypes.js_file import JsFile


class CharEncodedCount(Feature):

	_index_no: int = 21
	_name: str = "char_encoded_count"
	_var_type: type = int

	PATTERN = ""

	def _evaluate(self, js_file: JsFile) -> int:
		return len(re.findall(self.PATTERN, js_file.text))

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)

	

	def load_reserved_words(self):
		with open(JS_RESERVED_WORDS_PATH) as f:
			return [line.rstrip() for line in f]
