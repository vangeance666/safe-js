import os
import sys
import json
import esprima
from analyzer.core.exceptions import InvalidResourceError
from analyzer.datatypes.js_file import JsFile
from config import ERROR_DUMP_PATH


class JsStaticAnalyzer:

	name = "JsStaticAnalyzer"

	def _write_error_file(self, js_file: JsFile, error):
		save_path = os.path.join(ERROR_DUMP_PATH, js_file.src+".txt")
		with open(save_path, 'w') as f:
			f.write(js_file.text)

	def _run_syntactic_extraction(self, js_file: JsFile):

		if not js_file.text:
			raise InvalidResourceError("JS file does not have text")

		try:
			print("Type of text: ", type(js_file.text))
			js_file.syntactic_extract = esprima.parse(js_file.text)
		except Exception as e:
			try:
				print("Failed first try of syntactic extraction")
				print("Attempting second try with json.dumps")
				js_file.syntactic_extract = esprima.parse(json.dumps(js_file.text))
			except Exception as e2:
				raise


		js_file.synthetic_done = True
		js_file.static_done = True

	def run(self, js_file: JsFile) -> bool:

		try:
			self._run_syntactic_extraction(js_file)
		except Exception as e:
			print("Static Extraction Error: ", e)
			self._write_error_file(js_file, str(e))
			js_file.static_run_error = True
			return False
		return True
