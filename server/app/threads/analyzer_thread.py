
import itertools
import time
from collections import deque
from typing import List

from app.threads.worker import Worker
from analyzer.controllers.analysis_controller import AnalysisController
from analyzer.controllers.features_controller import FeaturesController

class AnalyzerThread(Worker):
	
	def __init__(self, thread_lock, pending_queue, analyzed_pages, platform_running):
		super().__init__(thread_lock, pending_queue, analyzed_pages, platform_running)

		self._analysis_controller = AnalysisController()
		self._features_controller = FeaturesController()

	def run(self):
		print("---started analyzer thread---")
		while self._do_run:
			self._thread_lock.acquire()
			for page in self._pending_pages:
				if page.status == "crawling" and page.crawl_success and not page.is_analyzed:
					print("Analyzer found one page", page.src)
					try:
						page.status = "analyzing"
						for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
							print("analyzing js file", js_file.src)

							self._analysis_controller.run_static_analysis(js_file)
							self._analysis_controller.run_dynamic_analysis(js_file)
							self._features_controller.extract_all_features(js_file)
							self._analysis_controller.cleanup()

						page.is_analyzed = True
						page.features_extracted = True
						page.status = "done"
					except Exception as e:
						print("AnalyzerThread error: ", e)
						page.status = "error"
						# raise

				# self._analyzed_pages.append(self._pending_pages.popleft())
			self._thread_lock.release()

			print("AnalyzerThread sleeping for 5 seconds")
			time.sleep(5)	
