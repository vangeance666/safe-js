import copy
import itertools
import threading
from collections import deque
from typing import List

from analyzer.controllers.results_controller import ResultsController
from analyzer.core.dataset_generator import DatasetGenerator
from analyzer.core.url_validator import UrlValidator
from analyzer.datatypes.js_file import JsFile
from analyzer.datatypes.page import Page
from app.threads.analyzer_thread import AnalyzerThread
from app.threads.cleaner_thread import CleanerThread
from app.threads.crawler_thread import CrawlerThread
from config import ANALYZED_PAGES_SAVE_PATH, PENDING_PAGES_SAVE_PATH


class NotFoundDetails(Exception):
	pass

class PlatformController:

	FEATURE_HEADERS = ['Index', "Feature Name", "Exists/NoError", "Value"]

	def __init__(self):

		self._platform_running: bool = True

		self.save_analyzed_path = ANALYZED_PAGES_SAVE_PATH
		self.save_pending_path = PENDING_PAGES_SAVE_PATH

		# self._dataset_generator = DatasetGenerator()
		self._results_controller = ResultsController()

		self._analyzed_pages: List[Pages] = self._results_controller.load_pages(
			self.save_analyzed_path) or []

		self._analysis_queue: deque = deque([])

		self._url_validator = UrlValidator()

		self._threads = [AnalyzerThread
			, CleanerThread
			, CrawlerThread
		]

		self._thread_lock = threading.Lock()

	def start_threads(self):
		for thread in self._threads:

			thread_obj = thread(self._thread_lock
				, self._analysis_queue
				, self._analyzed_pages
				, self._platform_running)

			thread_obj.start()

	def fetch_dashboard_details(self) -> dict:

		ret = {
			# Remember to implement logic
			"pages_analyzed": 0
			, "js_file_analysed": 0 # count in loop 
			, "predict_flagged_files": 0 # count in loop
			, "pages_with_error" : 0
			, "page_pending_count" : len(self._analysis_queue)
			, "js_file_error_count" : 0 # count in loop
		}

		for page in self._analyzed_pages:
			ret['pages_analyzed'] += 1
			ret['pages_with_error'] += int(page.status == "error")
			for js_file in itertools.chain(page.internal_js_files
				, page.external_js_files):
				ret['js_file_analysed'] += 1
				if js_file.static_run_error or js_file.dynamic_run_error:
					ret['js_file_error_count'] += 1
					continue
				if js_file.model_predicted and js_file.malign_percent > 0.5:
					ret['predict_flagged_files'] += 1
		return ret

	# ok for recent view
	def fetch_all_pages_details(self) -> list:

		ret = []
		for page in self._analyzed_pages:
			row = {}
			row['id'] = page.id
			row['page_url'] = page.src
			js_files = list(itertools.chain(
				page.internal_js_files, page.external_js_files))
			row['static_done'] = all(
				[js_file.static_done for js_file in js_files])
			row['dynamic_done'] = all(
				[js_file.dynamic_done for js_file in js_files])

			row['js_file_details'] = [{
				"id": js_file.id, "src": js_file.src, "static_features_done": js_file.static_features_done, "dynamic_features_done": js_file.dynamic_features_done
			} for js_file in js_files]

			ret.append(row)
		return ret

	# For analysis view
	def fetch_js_file_details(self, page_id: int, js_file_id: int) -> dict:

		ret = {
			"static_features": {}, "dynamic_features": {}, "predict_malign": ""
		}

		for page in self._analyzed_pages:
			if page.id == page_id:
				for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
					if js_file.id == js_file_id:

						ret['static_features']['headers'] = self.FEATURE_HEADERS
						ret['static_features']['data'] = [[i, item[0], item[1][0], item[1][1]]
														  for i, item in enumerate(js_file.static_features['all'].items())]
						ret['dynamic_features']['headers'] = self.FEATURE_HEADERS
						ret['dynamic_features']['data'] = [[i, item[0], item[1][0], item[1][1]]
														   for i, item in enumerate(js_file.dynamic_features['iocs'].items())]
						ret['predict_malign'] = js_file.malign_percent
						return ret
		return None

	# Handle from POST json
	def analyze_one_url(self, url: str) -> int:
		print("url: ", url)
		# Returns page ID that the url is assigned to.
		
		self._url_validator.check(url.strip())
		
		page = Page(src=url if url.startswith('http') else "http://"+url)
		page.id = max([P.id for P in self._analyzed_pages]+[P.id for P in self._analysis_queue], default=0)	+ 1	

		self._analysis_queue.append(page)

		return page.id


	def delete_past_data(self) -> bool:
		
		del self._analyzed_pages
		self._analyzed_pages = []

		del self._analysis_queue
		self._analysis_queue = []

		self._save_all()

		return True


	def _save_all(self) -> bool:
		return self._results_controller.save_pages(self._analyzed_pages
			, self.save_analyzed_path) and self._results_controller.save_pages(
			self._analysis_queue, self.save_pending_path)    

	def cleanup(self):
		self._platform_running = False  # to Stop all thteads
		self._save_all()
