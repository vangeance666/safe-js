import csv
from typing import List

import pandas as pd
from analyzer.datatypes.page import Page
from analyzer.features.javascript.dynamic import dynamic_features
from analyzer.features.javascript.static import static_features


class DatasetWriter:

	def __init__(self, save_path: str, field_names: list):
		self._csv_path = save_path
		self._field_names = field_names

	def __enter__(self):
		self.f = open(self._csv_path, 'w', newline='')

		self.writer = csv.DictWriter(self.f
			, field_names=self._field_names)

		return self.writer

	def __exit__(self, exc_type, exc_value, exc_tb):
		self.f.close()


class DatasetGenerator:

	def __init__(self):
		pass

	def _evalute_dynamic_headers(self):
		for d, f in dynamic_features.items():
			print (d,f)



	def _evalute_field_names(self) -> list:
		pass

	# Rows
	# js_file.src, internal_external, <all static class names>, <all dynamic class names>

	def pages_to_csv(self, pages: List[Page], csv_save_path: str) -> bool:
		with DatasetWriter(csv_save_path,) as writer:
			for page in pages:
				pass
