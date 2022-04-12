import os
from typing import List
import itertools

from analyzer.core.js_features_extractor import JsFeaturesExtractor
from analyzer.core.utils import get_file_buffer
from analyzer.datatypes.box_js_result import BoxJsResult
from analyzer.datatypes.js_file import JsFile
from analyzer.datatypes.page import Page

from config import DYNAMIC_DUMP_FLDR

class FeaturesController:
	
	def __init__(self, dynamic_dump_folder: str=None):
		self._js_features_extractor = JsFeaturesExtractor(dynamic_dump_folder 
			or DYNAMIC_DUMP_FLDR)		

	def extract_static_features(self, js_file: JsFile):
		try:
			self._js_features_extractor.extract_static_features(js_file)
			js_file.static_features_done = True
		except Exception as e:
			# raise
			print("extract_static_features error: ", e)
			js_file.static_features_error = True
			# raise			

	def extract_dynamic_features(self, js_file: JsFile):
		try:
			self._js_features_extractor.extract_dynamic_features(js_file)
		except Exception as e:
			# raise
			print("extract_dynamic_features error: ", e)
			js_file.dynamic_features_error = True
			# raise
			

	def extract_all_features(self, js_file):
		self.extract_static_features(js_file)
		self.extract_dynamic_features(js_file)




