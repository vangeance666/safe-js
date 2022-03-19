import re

from analyzer.abstracts import Feature
from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.datatypes.js_file import JsFile


class KeywordWscriptCount(Feature):

	_index_no: int = 19
	_name: str = "keyword_wscript_count"
	_var_type: type = int
	
	KEYWORD = "wscript"

	def _evaluate(self, js_file: JsFile) -> int:
		return js_file.text.upper().count(self.KEYWORD.upper())


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
