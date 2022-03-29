import csv
from collections import OrderedDict
from typing import List
import itertools
import pandas as pd
from analyzer.core.utils import cw2us, us2mc
from analyzer.datatypes.page import Page
from analyzer.features.javascript.dynamic import dynamic_features
from analyzer.features.javascript.static import static_features
from dataclasses import asdict

class DatasetWriter:

	def __init__(self, save_path: str, field_names: list):
		self._csv_path = save_path
		self._field_names = field_names

	def __enter__(self):
		self.f = open(self._csv_path, 'w', newline='')

		self.writer = csv.DictWriter(self.f, fieldnames=self._field_names)

		return self.writer

	def __exit__(self, exc_type, exc_value, exc_tb):
		self.f.close()


class DatasetGenerator:

	def __init__(self):
		self._headers = ["js_src"] + self._eval_static_features_headers() + self._eval_dynamic_features_headers()
		print("self._headers: ", self._headers)

	@staticmethod
	def no_feature_found_row(feature_category: dict):
		""" For JS features extractor to generate default values if
		file is not found. 
		
		Args:
		    feature_category (dict): Dictionary of features class definitions
		"""	
		cols_names = [cw2us(y.__name__) for x, y in feature_category.items()] 

		return DatasetGenerator.default_row(col_names)


	def _feature_format(self, e) -> tuple:
		return ("has_"+cw2us(e), cw2us(e))

	def _eval_static_features_headers(self) -> list:
		return list(itertools.chain.from_iterable(self._feature_format(S.__name__)
			for _, S in static_features.items()))

	def _eval_dynamic_features_headers(self) -> list:
		return list(itertools.chain.from_iterable(self._feature_format(S.__name__)
			for _, S in dynamic_features.items()))
	
	@staticmethod
	def default_row(self, col_names: list) -> dict:
		return { col_name:0 for col_name in col_names }


	def pages_to_csv(self, pages: List[Page], csv_save_path: str) -> bool:
		with DatasetWriter(csv_save_path, self._headers) as writer:
			for page in pages:
				for js_file in itertools.chain(page.internal_js_files, page.external_js_files):

					static_default = DatasetGenerator.default_row(self._eval_static_features_headers())
					dynamic_default = DatasetGenerator.default_row(self._eval_dynamic_features_headers())

					row_data = {**{ "js_src": js_file.src }, **static_default, **dynamic_default}
					

					if not js_file.static_run_error \
						and js_file.static_features \
						and js_file.static_features.get("all"):

						for name, value in js_file.static_features.get("all").items():
							row_data["has_"+name], row_data[name] = value


					if not js_file.dynamic_run_error \
						and js_file.dynamic_features:

						for feature_category, results_dict in js_file.dynamic_features.items():
							if not results_dict:
								continue

							for name, value in results_dict.items():
								row_data["has_"+name], row_data[name] = value

					writer.writerow(row_data)
					# print("row_data: ", row_data)
					# import sys
					# sys.exit()


