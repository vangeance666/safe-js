import re

from analyzer.abstracts import Feature
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima
from analyzer.datatypes.js_file import JsFile


class FuncLogCount(Feature):

	_index_no: int = 6
	_name: str = "func_log_count"
	_var_type: type = int

	PATTERN = ""

	# CONDITIONS = [ConditionsFactory.element_func_call_condition("dispatchEvent")]

	def _evaluate(self, js_file: JsFile) -> int:
		return js_file.text.count("console.log(")
		# return len(re.findall(self.PATTERN, js_buffer))

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)
