import re

from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.datatypes.js_file import JsFile


class CharPercentCount(Feature):

	_index_no: int = 24
	_name: str = "char_percent_count"
	_var_type: type = int

	PATTERN = "%"

	def _evaluate(self, js_file: JsFile) -> int:
		return js_file.text.count(self.PATTERN)
		# return len(re.findall(self.PATTERN, js_buffer))

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)

	
