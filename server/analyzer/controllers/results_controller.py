import itertools
import os
import pickle
from typing import Any, List

from analyzer.core.page_parser import PageParser
from analyzer.datatypes.page import Page

class ResultsController:

	def __init__(self):
		self._page_parser = PageParser()

	def reparse_script_elements(self, pages: List[Page]):
		for page in pages:
			page.parsed = self._page_parser.parse_script_results(page)

	def _pickle_load(self, file_path: str):
		with open(file_path, 'rb') as f:
			return pickle.load(f)
			
	def _pickle_dump(self, data, save_path: str):		
		
		
		with open(save_path, 'wb') as f:
			pickle.dump(data, f)

	def _flush_script_elements(self, pages: List[Page]):
		# Have to do this cause pickle cant save BS4 Elements
		for p in pages:
			p.text = ""
			p.script_elements = []
			for j in itertools.chain(p.internal_js_files, p.external_js_files):
				j.text = ""
				j.syntactic_extract = []

	def load_pages(self, pikle_dump_path) -> List[Page]:
		try:
			data = self._pickle_load(pikle_dump_path)
			self.reparse_script_elements(data)	
			return data
		except Exception as e:
			
			return []

	def save_pages(self, pages: List[Page], pickle_dump_path) -> bool:
		
		try:
			self._flush_script_elements(pages)
			self._pickle_dump(pages, pickle_dump_path)
		except Exception as e:
			raise
			return False
		return True




