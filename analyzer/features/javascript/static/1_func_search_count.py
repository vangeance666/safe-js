import re

from analyzer.abstracts import Feature
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima
from analyzer.datatypes.js_file import JsFile


class FuncSearchCount(Feature):

	_index_no: int = 1
	_name: str = "search_function_count"
	_var_type: type = int

	CONDITIONS = [
		ConditionsFactory.element_func_call_condition("search")
	]
	# PATTERN = JsExtractionPatterns.var_function("search")

	def _evaluate(self, js_file: JsFile):
		return sum(parse_esprima(js_file.syntactic_extract.body, cond) for cond in self.CONDITIONS)

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)
