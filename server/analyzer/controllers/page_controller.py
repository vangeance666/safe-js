import os
from typing import List

from analyzer.core.page_parser import PageParser
from analyzer.core.utils import save_file, sha_256_str, format_js_file_save
from analyzer.datatypes.page import Page

from config import PAGE_SAVE_FLDR

class PageController:
	
	def __init__(self):
		self._page_parser = PageParser()
		self._save_fldr = PAGE_SAVE_FLDR # os.path.join(os.getcwd(), "data", "js_dynamic_results")


	def save_js_files(self, pages: List[Page]) -> bool:
		for page in pages:
			
			for js_file in [*page.internal_js_files, *page.external_js_files]:

				js_file.page_id = page.id
				js_file.page_src = page.src # 

				save_path = format_js_file_save(self._save_fldr, page.id, js_file.id)

				if save_file(save_path, js_file.text):
					print("sucess save file")
					js_file.saved_path = save_path
					js_file.is_saved = True

			page.saved = True

		return True

	def save_js_file(self, page: Page):
			
		for js_file in [*page.internal_js_files, *page.external_js_files]:

			js_file.page_id = page.id
			js_file.page_src = page.src

			save_path = format_js_file_save(self._save_fldr, page.id, js_file.id)

			if save_file(save_path, js_file.text):
				print("sucess save file")
				js_file.saved_path = save_path
				js_file.is_saved = True

		page.saved = True

	# New
	def crawl_details(self, page: Page) -> Page:
		self._page_parser.extract_page_details(page)

	def extract_pages(self, urls: list) -> List[Page]:
		ret = []

		for url in urls:
			page = Page(src=url)
			ret.append(page)
			self._page_parser.extract_page_details(page)

		return ret

