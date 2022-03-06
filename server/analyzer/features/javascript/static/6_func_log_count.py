from analyzer.datatypes.js_file import JsFile
from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature
import re
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima


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

	@property
	def index_no(self):
		return self._index_no

	@property
	def name(self):
		return self._name	

	@property
	def var_type(self):
		return self._var_type

