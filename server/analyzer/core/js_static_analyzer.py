from analyzer.datatypes.js_file import JsFile

import esprima

class JsStaticAnalyzer:

	def run_syntactic_extraction(self, js_file: JsFile):

		if not js_file.text:
			raise Exception("JS file does not have text")

		try:
			js_file.syntactic_extract = esprima.parse(js_file.text)
		except Exception as e:
			raise e

		js_file.synthetic_done = True
		js_file.static_done = True