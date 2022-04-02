import os
from typing import List
import itertools

from analyzer.core.js_features_extractor import JsFeaturesExtractor
from analyzer.core.utils import get_file_buffer
from analyzer.datatypes.box_js_result import BoxJsResult
from analyzer.datatypes.js_file import JsFile
from analyzer.datatypes.page import Page


class FeaturesController:
	
	def __init__(self):
		self._features_extractor = JsFeaturesExtractor()		

	def extract_page_features(self, page: Page):
		for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
			if not js_file.static_run_error:
				self._features_extractor.extract_static_features(js_file)

			if not js_file.dynamic_run_error:
				self._features_extractor.extract_dynamic_features(js_file)

	def extract_static_features(self, js_file: JsFile):
		self._features_extractor.extract_static_features(js_file)

	def extract_dynamic_features(self, js_file: JsFile):
		self._features_extractor.extract_dynamic_features(js_file)

	# old
	# def extract_pages_features(self, pages: List[Page]) -> bool:

	# 	for page in pages:

	# 		if not page.success: #Ensure that its successfully scraped
	# 			print("Skiped {} since not success".format(page.src))
	# 			continue

	# 		for js_file in itertools.chain(page.internal_js_files, page.external_js_files):

	# 			print("Extracting features for {}".format(js_file.src))

	# 			if not js_file.dynamic_run_error:
	# 				print("Dynamic features for {}".format(js_file.src))

	# 				self._features_extractor.extract_dynamic_features(js_file)
	# 			else:
	# 				print("[!] Skipped Dynamic features for {}".format(js_file.src))


	# 			if not js_file.static_run_error:
	# 				print("Static features for {}".format(js_file.src))

	# 				self._features_extractor.extract_static_features(js_file)
	# 			else:
	# 				print("[!] Skipped Static features for {}".format(js_file.src))


	# 	return True




