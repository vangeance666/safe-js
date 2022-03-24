import os
from typing import List
import itertools

from analyzer.core.js_dynamic_analyzer import JsDynamicAnalyzer
from analyzer.core.js_static_analyzer import JsStaticAnalyzer
from analyzer.core.js_features_extractor import JsFeaturesExtractor
from analyzer.core.utils import get_file_buffer
from analyzer.datatypes.box_js_result import BoxJsResult
from analyzer.datatypes.js_file import JsFile
from analyzer.datatypes.page import Page


class FeaturesController:
	
	def __init__(self):

		self._dynamic_analyzer = JsDynamicAnalyzer()

		self._static_analyzer = JsStaticAnalyzer()

		self._features_extractor = JsFeaturesExtractor()	

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		self._dynamic_analyzer.cleanup()

	def save_pages_to_csv(self, pages: List[Page]):
		pass

	def extract_pages_features(self, pages: List[Page]) -> bool:

		for page in pages:

			if not page.success: #Ensure that its successfully scraped
				print("Skiped {} since not success".format(page.src))
				continue

			for js_file in itertools.chain(page.internal_js_files, page.external_js_files):

				print("Extracting features for {}".format(js_file.src))

				try:
					self._static_analyzer.run_syntactic_extraction(js_file)
					self._features_extractor.extract_static_features(js_file)
				except Exception as e:
					print("e: ", e)
					js_file.static_run_error = True
					continue

				try:
					self._dynamic_analyzer.run_box_js(js_file)
					self._features_extractor.extract_dynamic_features(js_file)
				except Exception as e:
					print("e: ", e)
					js_file.dynamic_run_error = True					
					continue

				print("fin js")
			
		return True




