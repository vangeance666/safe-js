import re

from analyzer.abstracts import Feature
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima
from analyzer.datatypes.js_file import JsFile


class FuncEncodeCount(Feature):

	_index_no: int = 21
	_name: str = "func_encode_count"
	_var_type: type = int
	_description = "Checks for how many btoa functions are in the code"

	CONDITIONS = [ConditionsFactory.element_func_call_condition("dispatchEvent")]
	
	# PATTERN = ""

	def _evaluate(self, js_file: JsFile) -> int:
		return js_file.text.count("btoa(")

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)
