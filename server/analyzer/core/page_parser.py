import os 
import requests
from typing import Union, Any

from bs4 import BeautifulSoup, ResultSet
from analyzer.datatypes.js_file import JsFile
from analyzer.datatypes.page import Page
from urllib.parse import urlparse


class PageParser:

	MSG_JS_RETRIEVE_FAIL = "Failed to retrieve JS Content"

	URL_START = ("http://", "https://")

	def __init__(self):
		self.save_path = ""

	def _format_internal_js_src(self, counter):
		return "internal_js_"+str(counter)

	def _get_formated_src(self, page_src, element_src) -> str:
		if not self._is_url(element_src):
			return ''.join([self._get_url_root_path(page_src), element_src])
		return element_src

	def _is_url(self, text):
		return text.lower().startswith(self.URL_START)
	
	def _get_url_root_path(self, url) -> str:
		parsed_url = urlparse(url)
		return ''.join([parsed_url.scheme, "://", parsed_url.netloc, "/"])

	def _request_url_html(self, obj: Any) -> bool:
		try:
			r = requests.get(obj.src, allow_redirects=True)
			if r.ok and r.text:
				obj.text = r.text

				return True
		except requests.exceptions.RequestException as e:
			print(e)
		return False
		
	def parse_script_results(self, obj: Any) -> bool:
		try:
			obj.script_elements = BeautifulSoup(obj.text, 'html.parser').find_all("script")
			return True
		except Exception as e:
			print(e)
		return False	

	def _extract_js_files(self, page: Page) -> bool:

		counter = 0

		for element in page.script_elements:

			js_file = JsFile()

			if element.has_attr('src') and element['src']:
				# External
				js_file.src = self._get_formated_src(page.src, element['src'])
				js_file.success = self._request_url_html(js_file)

				page.external_js_files.append(js_file)
			else:
				# Internal
				js_file.src = self._format_internal_js_src(counter)
				js_file.text = element.text

				page.internal_js_files.append(js_file)

				counter += 1

		return True	

	def extract_page_details(self, url: str) -> Page:

		page = Page(src=url)

		page.success = self._request_url_html(page)

		if not page.success:
			return page

		page.parsed = self.parse_script_results(page)

		if page.parsed and page.script_elements:
			page.extracted = self._extract_js_files(page)

		return page




