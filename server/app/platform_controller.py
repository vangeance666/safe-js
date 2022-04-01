import itertools
from collections import deque
from dataclasses import asdict
from typing import List

from analyzer.controllers.analysis_controller import AnalysisController
from analyzer.controllers.features_controller import FeaturesController
from analyzer.controllers.page_controller import PageController
from analyzer.controllers.results_controller import ResultsController
from analyzer.core.dataset_generator import DatasetGenerator
from analyzer.datatypes.js_file import JsFile
from analyzer.datatypes.page import Page


class NotFoundDetails(Exception):
	pass

class PlatformController:

	def __init__(self):
		self._dataset_generator = DatasetGenerator()
		self._page_controller = PageController()
		self._features_controller = FeaturesController()
		self._analysis_controller  = AnalysisController()
		self._results_controller = ResultsController()

		self._analyzed_pages: List[Pages] = []

		self._analysis_queue: deque = deque()

		self.load_analyzed_pages()

	def load_analyzed_pages(self):
		self._analyzed_pages = self._results_controller.load_pages()

	# ok
	def fetch_dashboard_details(self) -> dict:
		all_js_files = [js_file for page in self._analyzed_pages
			for js_file in itertools.chain(page.internal_js_files, page.external_js_files)]

		return {
			"pages_analysed": len(self._analyzed_pages)
			, "js_file_analysed": len(all_js_files)
			, "predict_flagged_files": 0 # Remember to implement logic
		}

	# ok for recent view
	def fetch_all_pages_details(self) -> list:

		ret = []

		for page in self._analyzed_pages:
			row = {}
			row['id'] = page.id
			row['page_url'] = page.src
			js_files = list(itertools.chain(page.internal_js_files, page.external_js_files))
			row['static_done'] = all([js_file.static_done for js_file in js_files])
			row['dynamic_done'] = all([js_file.dynamic_done for js_file in js_files])

			row['js_file_details'] = [ {
				"id":js_file.id
				, "src":js_file.src
				, "static_features_done" : js_file.static_features_done
				, "dynamic_features_done" : js_file.dynamic_features_done
				} for js_file in js_files]
				
			ret.append(row)
		return ret


	# For analysis view
	def fetch_js_file_details(self, page_id: int, js_file_id: int) -> dict:
		# ret = {
		# 	"page_id": page_id
		# 	, "js_file_id": js_file_id
		# }
		for page in self._analyzed_pages:
			if page.id == page_id:
				for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
					if js_file.id == js_file_id:
						return asdict(js_file)

		return None
