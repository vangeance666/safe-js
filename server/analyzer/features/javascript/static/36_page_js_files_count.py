import re

from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.datatypes.js_file import JsFile


class PageJsFilesCount(Feature):

	_index_no: int = 36
	_name: str = "page_js_files_count"
	_var_type: type = int

	# PATTERN = JsExtractionPatterns.files("js")

	def _evaluate(self, js_file: JsFile) -> int:
		return js_file.text.count(".js")
		# return len(re.findall(self.PATTERN, js_file.text))

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)

	
