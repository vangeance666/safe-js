from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature
import re


class CharBackslashCount(Feature):

	_index_no: int = 22
	_name: str = "char_backslash_count"
	_var_type: type = int

	PATTERN = "\\"

	def _evaluate(self, js_buffer):
		return js_buffer.count(self.PATTERN)
		# return len(re.findall(self.PATTERN, js_buffer))

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

