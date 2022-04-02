from analyzer.datatypes.js_file import JsFile
from analyzer.core.exceptions import InvalidResourceError

import esprima
import sys

class JsStaticAnalyzer:

	name = "JsStaticAnalyzer"

	def _run_syntactic_extraction(self, js_file: JsFile):

		if not js_file.text:
			raise InvalidResourceError("JS file does not have text")

		try:
			print("Type of text: ", type(js_file.text))
			js_file.syntactic_extract = esprima.parse(js_file.text)
		except Exception as e:
			raise

		js_file.synthetic_done = True
		js_file.static_done = True

	def run(self, js_file: JsFile) -> bool:

		try:
			self._run_syntactic_extraction(js_file)
		except Exception as e:
			print("Static Extraction Error: ", e)
			js_file.static_run_error = True
			return False
		return True