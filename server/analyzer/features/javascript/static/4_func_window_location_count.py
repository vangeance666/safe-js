import re

from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima
from analyzer.datatypes.js_file import JsFile


class FuncWindowLocationCount(Feature):

	_index_no: int = 4
	_name: str = "func_window_location_count"
	_var_type: type = int

	# CONDITIONS = [ConditionsFactory.element_func_call_condition("dispatchEvent")]
	# PATTERN = ""

	def _evaluate(self, js_file: JsFile) -> int:
		return js_file.text.count("window.location(")
		# return len(re.findall(self.PATTERN, js_buffer))

	def extract(self, js_file: JsFile):
		try:
			return 1, self._evaluate(js_file)
		except Exception as e:
			print(e)
			return 0, 0 

	
