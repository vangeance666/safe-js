from analyzer.datatypes.js_file import JsFile
from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature
import re


class CharSingleQuoteCount(Feature):

	_index_no: int = 31
	_name: str = "char_single_quote_count"
	_var_type: type = int

	PATTERN = "'"

	def _evaluate(self, js_file: JsFile) -> int:
		return js_file.content.count(self.PATTERN)


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

