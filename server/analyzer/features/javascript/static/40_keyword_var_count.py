import re
import esprima

from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature
from analyzer.config import JS_RESERVED_WORDS_PATH
from analyzer.core.utils import entropy as entropy_value


class KeywordVarCount(Feature):

	_index_no: int = 40
	_name: str = "keyword_var_count"
	_var_type: type = int

	def _evaluate(self, js_buffer):
		return sum(1 for x in esprima.tokenize(js_buffer) if x.type == 'Keyword' and x.value == "var")

	def extract(self, js_buffer):
		return self._evaluate(js_buffer)

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
