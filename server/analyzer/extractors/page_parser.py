import os 
import requests
from typing import Union

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

	def _is_url(self, text):
		return text.lower().startswith(self.URL_START)
	
	def _get_url_root_path(self, url) -> str:
		parsed_url = urlparse(url)
		return ''.join([parsed_url.scheme, "://", parsed_url.netloc, "/"])

	def _request_url_html(self, url) -> Union[str, None]:
		try:
			r = requests.get(url, allow_redirects=True)
			return r.text if r.ok and r.text else None
		except requests.exceptions.RequestException as e:
			return None
		
	def _get_script_results(self, page_html: str) -> Union[ResultSet, None]:
		try:
			return BeautifulSoup(page_html, 'html.parser').find_all("script")
		except Exception as e:
			return None

	def _extract_js_files(self, page: Page, ele_results: ResultSet):
		"""Parses page html and extracts all JS files details.
			Internal and external JS files contents will be extracted
		
		Args:
		    page (Page): Description
		    ele_results (ResultSet): Description		
		
		"""

		counter = 0

		for res in ele_results:
			if res.has_attr('src'):
				# External
				js_file = JsFile()

				js_file.src = res['src'] if self._is_url(res['src']) else ''.join([self._get_url_root_path(page.url), res['src']])					
				js_file.content = self._request_url_html(js_file.src) or self.MSG_JS_RETRIEVE_FAIL					

				page.external_js_files.append(js_file)
			else:
				# Internal
				page.internal_js_files.append(
					JsFile(src=self._format_internal_js_src(counter)
					, content=res.text)
				)

				counter += 1

	def get_page_details(self, url: str) -> Page:
		"""Parses url html content and extract JS file details
		
		Args:
		    url (str): URL to extract info from
		
		Returns:
		    Page: Page Object containing information about JS files and page data
		"""
		page = Page(url=url)		

		html_text = self._request_url_html(page.url)		

		if html_text:
			script_results = self._get_script_results(html_text)
			if script_results:
				self._extract_js_files(page, script_results)

		return page




