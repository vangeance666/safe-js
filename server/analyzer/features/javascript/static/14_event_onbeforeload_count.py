from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature
import re


class EventOnbeforeloadCount(Feature):

	_index_no: int = 14
	_name: str = "event_onbeforeload_count"
	_var_type: type = int

	PATTERN = JsExtractionPatterns.event("onbeforeload", "beforeload")

	def _evaluate(self, js_buffer):
		return len(re.findall(self.PATTERN, js_buffer))

	def extract(self, js_buffer):
		return self._evaluate(js_buffer)

	@property
	def index_no(self):
		return self._index_no

	@property
	def name(self):
		return self._name	

	@property
	def var_type(self):
		return self._var_type

