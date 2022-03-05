from analyzer.datatypes.js_file import JsFile
from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature
import re


class PagePhpFilesCount(Feature):

	_index_no: int = 37
	_name: str = "page_php_files_count"
	_var_type: type = int

	PATTERN =  JsExtractionPatterns.files("php")
	
	def _evaluate(self, js_file: JsFile) -> int:
		return len(re.findall(self.PATTERN, js_file.content))

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

