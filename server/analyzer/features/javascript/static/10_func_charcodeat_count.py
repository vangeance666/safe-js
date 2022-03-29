import re

from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima
from analyzer.datatypes.js_file import JsFile


class FuncCharcodeatCount(Feature):

	_index_no: int = 10
	_name: str = "func_charcodeat_count"
	_var_type: type = int

	_description: str = "Returns the number of count for str.charCodeAt(idx)"

	CONDITIONS = [ConditionsFactory.element_func_call_condition("charCodeAt")]
	# PATTERN = JsExtractionPatterns.var_function("charCodeAt", True)

	def _evaluate(self, js_file: JsFile) -> int:
		return sum(parse_esprima(js_file.syntactic_extract.body, cond) for cond in self.CONDITIONS)

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)


	
