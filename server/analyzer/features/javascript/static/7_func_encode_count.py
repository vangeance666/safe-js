import re
from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature

class FuncEncodeCount(Feature):

	_index_no: int = 7
	_name: str = "func_encode_count"
	_var_type: type = int

	_description = "Encode function count from btoa()"

	PATTERN = ""

	def _evaluate(self, js_buffer):
		return js_buffer.count("btoa(")

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
