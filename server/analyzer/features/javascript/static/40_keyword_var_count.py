import re

import esprima
from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.core.utils import entropy as entropy_value
from analyzer.datatypes.js_file import JsFile
from config import JS_RESERVED_WORDS_PATH


class KeywordVarCount(Feature):

	_index_no: int = 40
	_name: str = "keyword_var_count"
	_var_type: type = int

	def _evaluate(self, js_file: JsFile) -> int:
		return sum(1 for x in esprima.tokenize(js_file.text) if x.type == 'Keyword' and x.value == "var")

	def extract(self, js_file: JsFile):
		try:
			return 1, self._evaluate(js_file)
		except Exception as e:
			print(e)
			return 0, 0 

	@property
	def index_no(self):
		return self._index_no

	@property
	def name(self):
		return self._name

	@property
	def var_type(self):
		return self._var_type

	def load_reserved_words(self):
		with open(JS_RESERVED_WORDS_PATH) as f:
			return [line.rstrip() for line in f]
