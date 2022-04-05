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
		except Exception as e:
			print("e: ", e)
			js_file.static_run_error = True

	def run_dynamic_analysis(self, js_file: JsFile):
		try:
			self._dynamic_analyzer.run(js_file)
		except Exception as e:
			print("e: ", e)
			js_file.dynamic_run_error = True
	# New
	# def analyze_page_js_files(self, page: Page) -> bool:

	# 	if not page.crawl_success:
	# 		return False

	# 	for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
	# 		self.run_static_analysis(js_file)
	# 		self.run_dynamic_analysis(js_file)

	# 	return True

		# Analyze regardless of erorr
		# return all([self.analyze_js_file(js_file) 
		# 	for js_file in itertools.chain(page.internal_js_files, page.external_js_files)])

	# Olds
	# def analyze_pages_js_files(self, pages: List[Page]) -> bool:
	# 	for page in pages:

	# 		if not page.crawl_success: #Ensure that its successfully scraped
	# 			print("Skiped {} since not success".format(page.src))
	# 			continue

	# 		for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
	# 			print("Attemping to extract features for {}".format(js_file.src))
	# 			for analyzer in self.analyzers:
	# 				print("Extracting analysis results using {}".format(analyzer.__class__))
	# 				analyzer.run(js_file)
					
	# 		page.is_analyzed = True			
	# 	return True

