from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature
import re


class FuncLogCount(Feature):

	_index_no: int = 6
	_name: str = "func_log_count"
	_var_type: type = int

	PATTERN = ""

	def _evaluate(self, js_buffer):
		return js_buffer.count("console.log(")
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

