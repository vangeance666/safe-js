import re

from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima
from analyzer.datatypes.js_file import JsFile


class FuncDecodeCount(Feature):

	_index_no: int = 7
	_name: str = "func_decode_count"
	_var_type: type = int

	_description = "Detect decode function count from atob()"

	CONDITIONS = [ConditionsFactory.element_func_call_condition("dispatchEvent")]
	
	PATTERN = ""

	def _evaluate(self, js_file: JsFile) -> int:
		return js_file.text.count("atob(")

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)

	
