import re

from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima
from analyzer.datatypes.js_file import JsFile


class FuncDispatcheventCount(Feature):

	_index_no: int = 16
	_name: str = "func_dispatchevent_count"
	_var_type: type = int

	CONDITIONS = [ConditionsFactory.element_func_call_condition("dispatchEvent")]
	
	# https://developer.mozilla.org/en-US/docs/Web/Events/Creating_and_triggering_events
	# PATTERN = JsExtractionPatterns.event("dispatchEvent", "build")

	def _evaluate(self, js_file: JsFile) -> int:
		return sum(parse_esprima(js_file.syntactic_extract.body, cond) for cond in self.CONDITIONS)

	def extract(self, js_file: JsFile):
		try:
			return 1, self._evaluate(js_file)
		except Exception as e:
			print(e)
			return 0, 0 

	
