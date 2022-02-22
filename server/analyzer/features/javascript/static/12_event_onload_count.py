import re
from analyzer.datatypes.js_file import JsFile
from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima


class EventOnloadCount(Feature):

	_index_no: int = 12
	_name: str = "event_onload_count"
	_var_type: type = int

	CONDITIONS = [
		ConditionsFactory.add_event_listener_condition("load")
		, ConditionsFactory.on_event_assign_condition("onload")
	]

	# PATTERN = JsExtractionPatterns.event("onload", "load")

	def _evaluate(self, js_file: JsFile) -> int:
		return sum(parse_esprima(js_file.body, cond) for cond in self.CONDITIONS)

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

