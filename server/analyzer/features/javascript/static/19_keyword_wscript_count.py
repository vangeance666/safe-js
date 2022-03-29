import re

from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
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

	
