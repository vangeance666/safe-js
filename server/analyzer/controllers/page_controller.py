import os
from typing import List

from analyzer.core.page_parser import PageParser
from analyzer.core.utils import save_file, sha_256_str, format_js_file_save
from analyzer.datatypes.page import Page

from config import PAGE_SAVE_FLDR

class PageController:
	
	def __init__(self):
		self._page_parser = PageParser()
		self._save_fldr = PAGE_SAVE_FLDR

	def save_js_files(self, pages: List[Page]) -> bool:
		for page in pages:

			folder_name = sha_256_str(page.src)
			
			for js_file in [*page.internal_js_files, *page.external_js_files]:

				js_file.page_src = page.src

				save_path = format_js_file_save(self._save_fldr, js_file)
				# save_path = os.path.join(self._save_fldr
				# 		, folder_name
				# 		, sha_256_str(js_file.src))

				print("save_path: ", save_path)

				if save_file(save_path, js_file.text):
					print("sucess save file")
					js_file.saved_path = save_path
					# js_file.rel_path = '\\'.join(save_path.split('\\')[-2:])
					js_file.is_saved = True


			page.saved = True

		return True

	def extract_pages(self, urls: list) -> List[Page]:
		return [self._page_parser.extract_page_details(url=url) for url in urls]
