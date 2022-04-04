import csv
from collections import OrderedDict
from typing import List
import itertools
import pandas as pd
from analyzer.core.utils import cw2us, us2mc
from analyzer.datatypes.page import Page
from analyzer.datatypes.js_file import JsFile
from analyzer.features.javascript.dynamic import dynamic_features
from analyzer.features.javascript.static import static_features
from dataclasses import asdict

class DatasetWriter:

	def __init__(self, save_path: str, mode: str, field_names: list):
		self._csv_path = save_path
		self._mode = mode
		self._field_names = field_names

	def __enter__(self):
		
		self.f = open(self._csv_path, self._mode, newline='')
		self.writer = csv.DictWriter(self.f, fieldnames=self._field_names)

		return self.writer

	def __exit__(self, exc_type, exc_value, exc_tb):
		self.f.close()


class DatasetGenerator:

	def __init__(self):
		self._headers = ["js_src"] + self._eval_static_features_headers() + self._eval_dynamic_features_headers()
		

	@staticmethod
	def no_feature_found_row(feature_category: dict) -> dict:
		""" For JS features extractor to generate default values if
		file is not found. 
		
		Args:
		    feature_category (dict): Dictionary of features class definitions
		"""	
		col_names = [cw2us(y.__name__) for x, y in feature_category.items()] 

		return {col_name: (0,0) for col_name in col_names}

	def _feature_format(self, e) -> tuple:
		return ("has_"+cw2us(e), cw2us(e))

	def _eval_static_features_headers(self) -> list:
		return list(itertools.chain.from_iterable(self._feature_format(S.__name__)
			for _, S in static_features.items()))

	def _eval_dynamic_features_headers(self) -> list:
		return list(itertools.chain.from_iterable(self._feature_format(S.__name__)
			for _, S in dynamic_features.items()))
	
	def default_vals(self, col_names: list) -> dict:
		return { col_name:0 for col_name in col_names }

	# Use for one single js file too before inference later on.
	def eval_js_file_row(self, js_file: JsFile) -> dict:
		static_default = self.default_vals(self._eval_static_features_headers())
		dynamic_default = self.default_vals(self._eval_dynamic_features_headers())

		row_data = {**{ "js_src": js_file.src }, **static_default, **dynamic_default}					

		if not js_file.static_run_error and js_file.static_features and js_file.static_features.get("all"):
			for name, values in js_file.static_features.get("all").items():
				row_data["has_"+name], row_data[name] = values

		if not js_file.dynamic_run_error and js_file.dynamic_features:
			for feature_category, results_dict in js_file.dynamic_features.items():
				if not results_dict: # Skip if dict is totally empty meaning file not found
					continue
				for name, value in results_dict.items():
					
					row_data["has_"+name], row_data[name] = value

		return row_data

	def js_files_to_csv(self, js_files: List[JsFile], csv_save_path) -> bool:
		with DatasetWriter(csv_save_path, self._headers) as writer:
			for js_file in js_files:
				row_data = self.eval_js_file_row(js_file)
				writer.writerow(row_data)
		return True

	def pages_to_csv(self, pages: List[Page], csv_save_path: str) -> bool:
		with DatasetWriter(csv_save_path, 'w', self._headers) as writer:
			writer.writeheader()
			for page in pages:
				for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
					row_data = self.eval_js_file_row(js_file)
					writer.writerow(row_data)
	

	def write_header_csv(self, csv_save_path: str):
		with DatasetWriter(csv_save_path, 'w', self._headers) as writer:
			writer.writeheader()

	def append_js_file_to_csv(self, js_files: List[JsFile], csv_save_path: str):
		with DatasetWriter(csv_save_path, 'a',  self._headers) as writer:
			row_data = self.eval_js_file_row(js_file)
			writer.writerow(row_data)
			
	def append_pages_to_csv(self, pages: List[Page], csv_save_path: str):
		with DatasetWriter(csv_save_path, 'a',  self._headers) as writer:
			for page in pages:
				for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
					row_data = self.eval_js_file_row(js_file)
					writer.writerow(row_data)
					# import sys
					# sys.exit()


