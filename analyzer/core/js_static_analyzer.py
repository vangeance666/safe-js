import os
import sys
import json
import esprima
from analyzer.core.exceptions import InvalidResourceError
from analyzer.datatypes.js_file import JsFile
from config import ERROR_DUMP_PATH


class JsStaticAnalyzer:

	name = "JsStaticAnalyzer"

	def _run_syntactic_extraction(self, js_file: JsFile) -> None:

		try:
			js_file.syntactic_extract = esprima.parse(js_file.text)
		except Exception as e:
			print("_run_syntactic_extraction error: ", e)
			return

		js_file.synthetic_done = True

	def run(self, js_file: JsFile) -> None:
		
		if not js_file.text:
			raise InvalidResourceError("JS file does not have text")

		self._run_syntactic_extraction(js_file)	

		if not js_file.synthetic_done:
			print("Trying second try with json encoded text")
			js_file.text = json.dumps(js_file.text)
			self._run_syntactic_extraction(js_file)	

		js_file.static_done = True