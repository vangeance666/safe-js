import copy
import itertools
from collections import deque
from typing import List

from analyzer.controllers.results_controller import ResultsController
from analyzer.core.dataset_generator import DatasetGenerator
from analyzer.datatypes.js_file import JsFile
from analyzer.datatypes.page import Page
from config import ANALYZED_PAGES_SAVE_PATH, PENDING_PAGES_SAVE_PATH

from app.threads.analyzer_thread import AnalyzerThread

class NotFoundDetails(Exception):
	pass



class PlatformController:

	FEATURE_HEADERS = ['Index', "Feature Name", "Exists/NoError", "Value"]

	def __init__(self):

		self._platform_running: bool = True

		self.save_analyzed_path = ANALYZED_PAGES_SAVE_PATH
		self.save_pending_path = PENDING_PAGES_SAVE_PATH
		
		self._dataset_generator = DatasetGenerator()
		self._results_controller = ResultsController()

		self._analyzed_pages: List[Pages] = self._results_controller.load_pages(ANALYZED_PAGES_SAVE_PATH) or []

		self._analysis_queue: deque = deque([])

		self._threads = [
			AnalyzerThread(self._analysis_queue, self._analyzed_pages, self._platform_running)
		]


	def start_threads(self):
		for thread in self._threads:
			thread.start()
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
		
		ret = {
			"static_features": {}
			, "dynamic_features": {}
			, "predict_malign": ""
		} 
		
		for page in self._analyzed_pages:
			if page.id == page_id:
				for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
					if js_file.id == js_file_id:
						
						ret['static_features']['headers'] = self.FEATURE_HEADERS
						ret['static_features']['data'] = [ [i, item[0], item[1][0], item[1][1]] for i, item in enumerate(js_file.static_features['all'].items())]
						ret['dynamic_features']['headers'] = self.FEATURE_HEADERS
						ret['dynamic_features']['data'] = [ [i, item[0], item[1][0], item[1][1] ] for i, item in enumerate(js_file.dynamic_features['iocs'].items())]
						ret['predict_malign'] = js_file.malign_percent
						return ret
		return None


	

	def _save_analysed_pages(self) -> bool:
		return self._results_controller.save_pages(
			self._analyzed_pages, self.save_analyzed_path)

	def _save_pending_pages(self) -> bool:
		return self._results_controller.save_pages(
			self._analysis_queue, self.save_pending_path)

	def _save_all(self) -> bool:
		self._save_analysed_pages()
		self._save_pending_pages()

	def delete_past_data(self) -> bool:
		del self._analyzed_pages
		self._analyzed_pages = []
		self._save_all()

	def cleanup(self): 
		self._platform_running = False # to Stop all thteads
		self._save_all()
