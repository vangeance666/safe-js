import re

from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima
from analyzer.datatypes.js_file import JsFile


class EventOnbeforeunloadCount(Feature):

	_index_no: int = 11
	_name: str = "event_onbeforeunload_count"
	_var_type: type = int

	CONDITIONS = [
		ConditionsFactory.add_event_listener_condition("beforeunload")
		,ConditionsFactory.on_event_assign_condition("onbeforeunload")
	]

	# PATTERN = JsExtractionPatterns.event("onbeforeunload", "beforeunload")
	
	def _evaluate(self, js_file: JsFile) -> int:
		return sum(parse_esprima(js_file.syntactic_extract.body, cond) for cond in self.CONDITIONS)

	def extract(self, js_file: JsFile):

		return self._evaluate(js_file)

	
