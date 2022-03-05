from analyzer.datatypes.js_file import JsFile
import re
from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima


class FuncDecodeCount(Feature):

	_index_no: int = 7
	_name: str = "func_decode_count"
	_var_type: type = int

	_description = "Detect decode function count from atob()"

	CONDITIONS = [ConditionsFactory.element_func_call_condition("dispatchEvent")]
	
	PATTERN = ""

	def _evaluate(self, js_file: JsFile) -> int:
		return js_file.content.count("atob(")

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
