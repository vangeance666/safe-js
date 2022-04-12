import itertools
from typing import List
from analyzer.core.js_dynamic_analyzer import JsDynamicAnalyzer

from analyzer.datatypes.page import Page
from analyzer.datatypes.js_file import JsFile

from analyzer.core.js_static_analyzer import JsStaticAnalyzer

from config import DYNAMIC_DUMP_FLDR


class AnalysisController:

	def __init__(self, dynamic_dump_folder=None):

		self._static_analyzer = JsStaticAnalyzer()
		self._dynamic_analyzer = JsDynamicAnalyzer(dynamic_dump_folder or DYNAMIC_DUMP_FLDR)

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		self._dynamic_analyzer.cleanup()

	def cleanup(self):
		self._dynamic_analyzer.cleanup()

	def analyze_js_file(self, js_file: JsFile) -> List[bool]:
		return [analyzer.run(js_file) for analyzer in self.analyzers]	

	def run_static_analysis(self, js_file: JsFile):
		try:
			self._static_analyzer.run(js_file)
			js_file.static_features_done = True
		except Exception as e:
			print("e: ", e)
			js_file.static_run_error = True

	def run_dynamic_analysis(self, js_file: JsFile):
		try:
			self._dynamic_analyzer.run(js_file)
			js_file.dynamic_features_done = True
		except Exception as e:
			print("e: ", e)
			js_file.dynamic_run_error = True