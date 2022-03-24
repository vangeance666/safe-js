import itertools
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

	def _pickle_dump(self, save_path: str, data):
		with open(save_path, 'wb') as f:
			pickle.dump(data, f)
			# pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

	def _flush_script_elements(self, pages: List[Page]):
		# Have to do this cause pickle cant save BS4 Elements
		for p in pages:
			p.text = ""
			p.script_elements = []
			for j in itertools.chain(p.internal_js_files, p.external_js_files):
				j.text = ""
				j.syntactic_extract = []


	def load_pages(self) -> List[Page]:
		
		if not os.path.exists(self._pages_results_path):
			return None

		data = self._pickle_load(self._pages_results_path)
		self.reparse_script_elements(data)
		
		return data 
		


	def save_pages(self, pages: List[Page]) -> bool:
		try:
			if pages is None:
				print('Pages is none')

			self._flush_script_elements(pages)

			if pages is None:
				print('Pages is none')

			self._pickle_dump(self._pages_results_path, pages)
		except Exception as e:
			raise
		return True
