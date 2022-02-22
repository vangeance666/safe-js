from analyzer.datatypes.js_file import JsFile
from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature
from analyzer.config import JS_RESERVED_WORDS_PATH
from analyzer.core.utils import entropy as entropy_value
import re

class FileEntropyValue(Feature):

	_index_no: int = 21
	_name: str = "file_entropy_value"
	_var_type: type = int

	def _evaluate(self, js_file: JsFile) -> int:
		return entropy_value(js_file.content)

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
