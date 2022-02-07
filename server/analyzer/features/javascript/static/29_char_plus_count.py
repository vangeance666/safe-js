
from dataclasses import dataclass
from analyzer.abstracts.feature import Feature
import re


class CharPlusCount(Feature):

	_index_no: int = 29
	_name: str = "char_plus_count"
	_var_type: type = int

	PATTERN = ""

	def _evaluate(self, js_buffer):
		return len(re.findall(self.PATTERN, js_buffer))

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

