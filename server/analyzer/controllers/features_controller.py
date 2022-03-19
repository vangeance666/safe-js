import os
from typing import List

import esprima
from analyzer.core.js_dynamic_analyzer import BoxJsResponse, JsDynamicAnalyzer
from analyzer.core.utils import get_file_buffer
from analyzer.datatypes.box_js_result import BoxJsResult
from analyzer.datatypes.js_file import JsFile
from analyzer.datatypes.page import Page
from analyzer.features.javascript.static import static_features


class FeaturesController:
	
	def __init__(self):
		self._dynamic_analyzer = JsDynamicAnalyzer()

		self._static_features = static_features
		self.sequence = {}

		self.saved_js_paths: list = []

	def _run_syntactic_extraction(self, js_file: JsFile) -> bool:
		try:
			js_file.syntactic_extract = esprima.parse(js_file.text)
		except:
			return False
		return True

	def _extract_static_features(self, js_file: JsFile) -> bool:

		if not js_file.text:
			return False

		print("Extracting static features for :", js_file.src)

		for x in self._static_features:
			print("Currently extracting: ", x)

			x_obj = self._static_features[x]()
			js_file.static_features[x_obj.name] = x_obj.extract(js_file)

		return True

	def _extract_dynamic_features(self, js_file: JsFile) -> BoxJsResult:
		""" first checks if js_file is successfully saved. 
		After that send to box-js for analysis and retrieve information

		Args:
		    js_file (JsFile): Description
		
		Returns:
		    bool: Description
		"""
		# First check if file is saved at location,

		print("js_file.saved_path: ", js_file.saved_path)	

		try:
			self._dynamic_analyzer.analyze(js_file)
		except Exception as e:
			raise e
			# return None
		
		if not js_file.dynamic_done:
			return None





		# if res == BoxJsResponse.SUCCESS:
		# 	pass

	def extract_pages_features(self, pages: List[Page]) -> bool:

		for page in pages:

			if not page.success: #Ensure that its successfully scraped
				continue

			for js_file in page.external_js_files:

				if not js_file.text: #Ensure that js file is parsed
					print("if not js_file.text:")
					continue

				# # print(js_file.text)
				# if not self._run_syntactic_extraction(js_file): 
				# 	print("if not self._run_syntactic_extraction(js_file):")
				# 	continue

				# # After extracting all the syntactic details, then extract static details
				
				# if not self._extract_static_features(js_file):
				# 	print("Failed to retrieve static features forP: ", js_file.src)
				# 	continue

				print("before dynamic, ", js_file.saved_path)
				if not self._extract_dynamic_features(js_file):
					print("failed to retrieve dynamic features for: ", js_file.src)
					continue

				print("fin js")

				# if js_file.src == "https://developer.mozilla.org//static/js/4.a756dea3.chunk.js":
				# 	print("Doing extract")
				
			
		return True
