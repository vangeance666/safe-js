import os

from analyzer.core.page_parser import PageParser
from typing import List
from analyzer.datatypes.page import Page
from analyzer.config import PAGE_SAVE_FLDR

import hashlib

class PageController:
	

	def __init__(self):
		self._page_parser = PageParser()
		self._save_fldr = PAGE_SAVE_FLDR

	def _hash(self, text) -> str:
		return hashlib.sha256(text.encode()).hexdigest()

	def _save_file(self, file_name: str, text: str) -> bool:
		try:
			with open(file_name, 'w') as f:
				f.write(text)
		except Exception as e:
			return False
		return True

	def save_js_files(self, pages: List[Page]) -> bool:
		for page in pages:

			fldr_name = self._hash(page.url)
			
			for js_file in [*page.internal_js_files, *page.external_js_files]:
				self._save_file(
					os.path.join(self._save_fldr, fldr_name, self._hash(js_file.src))
					, js_file.text)

			page.saved = True

		return True


	def extract_pages(self, urls: list) -> List[Page]:
		print("page controlle4r: urls: ", urls)
		return [self._page_parser.extract_page_details(url=url) for url in urls]
