import os
import pickle
from typing import Any, List

from analyzer.core.page_parser import PageParser
from analyzer.datatypes.page import Page
from config import RESULTS_SAVED_PATH


class ResultsController:

	def __init__(self):
		self._pages_results_path = RESULTS_SAVED_PATH
		self._page_parser = PageParser()

	def reparse_script_elements(self, pages: List[Page]):
		for page in pages:
			page.parsed = self._page_parser.parse_script_results(page)

	def _pickle_load(self, file_path: str):
		with open(file_path, 'rb') as f:
			return pickle.load(f)

	def _pickle_dump(self, save_path: str, data: Any):
		with open(save_path, 'wb') as f:
			pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

	def _flush_script_elements(self, pages: List[Page]):
		# Have to do this cause pickle cant save BS4 Elements
		for p in pages:
			p.script_elements = None

	def load_pages(self) -> List[Page]:
		
		if not os.path.exists(self._pages_results_path):
			return None
		
		return self.reparse_script_elements(self._pickle_load(self._pages_results_path))
		


	def save_pages(self, pages: List[Page]) -> bool:
		try:
			self._flush_script_elements(pages)
			self._pickle_dump(self._pages_results_path, data=pages)
		except Exception as e:
			raise
		return True
