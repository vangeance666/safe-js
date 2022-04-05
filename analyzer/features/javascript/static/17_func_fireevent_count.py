import re

from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima
from analyzer.datatypes.js_file import JsFile


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

	
