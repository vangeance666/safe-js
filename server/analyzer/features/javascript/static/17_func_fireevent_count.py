import re
from analyzer.datatypes.js_file import JsFile
from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima


class FuncFireeventCount(Feature):

	_index_no: int = 17
	_name: str = "event_fireevent_count"
	_var_type: type = int

	CONDITIONS = [
		ConditionsFactory.element_func_call_condition("fireEvent")
	]

	# https://stackoverflow.com/questions/2490825/how-to-trigger-event-in-javascript
	# https://www.vbsedit.com/html/ce2dd21d-bfe5-4987-a313-d1284de606fd.asp
	# PATTERN = JsExtractionPatterns.normal_function("fireEvent")

	def _evaluate(self, js_file: JsFile) -> int:
		return sum(parse_esprima(js_file.syntactic_extract.body, cond) for cond in self.CONDITIONS)

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)

	@property
	def index_no(self):
		return self._index_no

	@property
	def name(self):
		return self._name	

	@property
	def var_type(self):
		return self._var_type