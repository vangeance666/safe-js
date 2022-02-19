from analyzer.core.js_extraction_patterns import JsExtractionPatterns
from analyzer.abstracts.feature import Feature
from analyzer.config import JS_RESERVED_WORDS_PATH
import re


class KnownWordsCount(Feature):

	_index_no: int = 21
	_name: str = "known_words_count"
	_var_type: type = int

	PATTERN = ""

	def __init__(self):
		self.reserved_words = self.load_reserved_words()

	def _evaluate(self, js_buffer):
		buf = js_buffer
		
		for word in self.reserved_words:
			buf = buf.replace(word, "")

		print("buf: ", buf)
		# After replace then detect how many used english words	

	def extract(self, js_buffer):
		return self._evaluate(js_buffer)

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