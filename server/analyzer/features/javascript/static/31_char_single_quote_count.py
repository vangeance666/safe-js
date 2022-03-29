import re

from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.datatypes.js_file import JsFile


class CharSingleQuoteCount(Feature):

	_index_no: int = 31
	_name: str = "char_single_quote_count"
	_var_type: type = int

	PATTERN = "'"

	def _evaluate(self, js_file: JsFile) -> int:
		return js_file.text.count(self.PATTERN)


	def extract(self, js_file: JsFile):
		try:
			return 1, self._evaluate(js_file)
		except Exception as e:
			print(e)
			return 0, 0 

	
