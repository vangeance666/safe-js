import re

from analyzer.abstracts import Feature
from analyzer.datatypes.js_file import JsFile


class CharCloseBraceCount(Feature):

	_index_no: int = 35
	_name: str = "char_close_brace_count"
	_var_type: type = int

	PATTERN = "}"

	def _evaluate(self, js_file: JsFile) -> int:
		return js_file.text.count(self.PATTERN)

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)
