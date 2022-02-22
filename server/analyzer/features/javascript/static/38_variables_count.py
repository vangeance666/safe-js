from analyzer.datatypes.js_file import JsFile
from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature
from analyzer.config import JS_RESERVED_WORDS_PATH
import re
import esprima




class VariablesCount(Feature):

	_index_no: int = 38
	_name: str = "variables_count"
	_var_type: type = int
	_description = "count number of variables witin js file"

	def __init__(self):
		self.reserved_words = self.load_reserved_words()

	def _evaluate(self, js_file: JsFile) -> int:
		return sum(1 for x in esprima.tokenize(js_file.content) if x.type == "Identifier")

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

	def load_reserved_words(self):
		with open(JS_RESERVED_WORDS_PATH) as f:
			return [line.rstrip() for line in f]