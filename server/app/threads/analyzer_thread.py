
import threading
import time
from collections import deque
from typing import List
import itertools

from analyzer.controllers.analysis_controller import AnalysisController
from analyzer.controllers.features_controller import FeaturesController
from analyzer.controllers.page_controller import PageController


class AnalyzerThread(threading.Thread):
	
	def __init__(self, pending_queue, analyzed_pages, platform_running):
		super().__init__()

		self._pending_pages: deque = pending_queue
		self._analyzed_pages: List[Page] = analyzed_pages

		self._do_run: bool = platform_running

		self._page_controller 		= PageController()
		self._features_controller 	= FeaturesController()
		self._analysis_controller  	= AnalysisController()	

	def run(self):
		print("started analyzer thread")
		while self._do_run:
			if len(self._pending_pages) > 0:

				page = self._pending_pages[0] # dont remove from queue first
				print("Found one in analysis queue {}", page.src)

				self._page_controller.crawl_details(page)
				self._page_controller.save_js_file(page)

				self._analysis_controller.analyze_page_js_files(page)

				for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
					try:
						self._features_controller.extract_static_features(js_file)
					except Exception as e:
						print(e)

					try:
						self._features_controller.extract_dynamic_features(js_file)
					except Exception as e:
						print(e)

				# Once finished	then transfer over incase when close app while 
				self._analyzed_pages = self._pending_pages.popleft()

			print("Sleeping for 5 seconds")
			time.sleep(5) # Repeat check every 5 secs to prevent clogging		
