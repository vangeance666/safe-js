import re

import esprima
from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.datatypes.js_file import JsFile
from config import JS_RESERVED_WORDS_PATH


class VariablesCount(Feature):

	_index_no: int = 38
	_name: str = "variables_count"
	_var_type: type = int
	_description = "count number of variables witin js file"

	def __init__(self):
		self.reserved_words = self.load_reserved_words()

	def _evaluate(self, js_file: JsFile) -> int:
		return sum(1 for x in esprima.tokenize(js_file.text) if x.type == "Identifier")

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)

	

	def load_reserved_words(self):
		with open(JS_RESERVED_WORDS_PATH) as f:
			return [line.rstrip() for line in f]
