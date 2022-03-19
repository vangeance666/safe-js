import re

from analyzer.abstracts import Feature
from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima
from analyzer.datatypes.js_file import JsFile


class EventOnmouseoverCount(Feature):

	_index_no: int = 15
	_name: str = "event_onmouseover_count"
	_var_type: type = int

	CONDITIONS = [
		ConditionsFactory.add_event_listener_condition("mouseover")
		, ConditionsFactory.on_event_assign_condition("onmouseover")
	]
	
	# PATTERN = JsExtractionPatterns.event("onmouseover", "mouseover")

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
