import re

from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.datatypes.js_file import JsFile


class PagePhpFilesCount(Feature):

	_index_no: int = 37
	_name: str = "page_php_files_count"
	_var_type: type = int

	# PATTERN =  JsExtractionPatterns.files("php")
	
	def _evaluate(self, js_file: JsFile) -> int:
		return js_file.text.count(".php")
		# return len(re.findall(self.PATTERN, js_file.text))

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)

	
