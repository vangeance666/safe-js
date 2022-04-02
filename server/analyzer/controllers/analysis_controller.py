import itertools
from typing import List
from analyzer.core.js_dynamic_analyzer import JsDynamicAnalyzer

from analyzer.datatypes.page import Page
from analyzer.datatypes.js_file import JsFile

from analyzer.core.js_static_analyzer import JsStaticAnalyzer



class AnalysisController:

	def __init__(self):
		self._dynamic_analyzer = JsDynamicAnalyzer()
		self._static_analyzer = JsStaticAnalyzer()

		self.analyzers = [
			self._static_analyzer
			, self._dynamic_analyzer
		]

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		self._dynamic_analyzer.cleanup()		

	def _apply_all_analyzers(self, js_file: JsFile) -> list:
		return [analyzer.run(js_file) for analyzer in self.analyzers]	

	# New
	def analyze_page_js_files(self, page: Page) -> bool:

		if not page.success:
			return False

		# Analyze regardless of erorr
		return all([self._apply_all_analyzers(js_file) 
			for js_file in itertools.chain(page.internal_js_files, page.external_js_files)])

	# Olds
	# def analyze_pages_js_files(self, pages: List[Page]) -> bool:
	# 	for page in pages:

	# 		if not page.success: #Ensure that its successfully scraped
	# 			print("Skiped {} since not success".format(page.src))
	# 			continue

	# 		for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
	# 			print("Attemping to extract features for {}".format(js_file.src))
	# 			for analyzer in self.analyzers:
	# 				print("Extracting analysis results using {}".format(analyzer.__class__))
	# 				analyzer.run(js_file)
					
	# 		page.is_analyzed = True			
	# 	return True

