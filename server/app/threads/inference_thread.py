import itertools
import time
from collections import deque
from typing import List

# from analyzer.controllers.analysis_controller import AnalysisController
# from analyzer.controllers.features_controller import FeaturesController


from app.models.processing_status import ProcessingStatus
from app.threads.worker import Worker


class InferenceThread(Worker):
	
	def __init__(self, thread_lock, pending_queue, analyzed_pages, platform_running):
		super().__init__(thread_lock, pending_queue, analyzed_pages, platform_running)

		# self._analysis_controller = AnalysisController()
		# self._features_controller = FeaturesController()

	def run(self):
		print("---started analyzer thread---")
		while self._do_run:
			self._thread_lock.acquire()
			for page in self._pending_pages:
				if page.status == ProcessingStatus.ANALYZING \
					and page.is_analyzed \
					and page.features_extracted:

					try:
						page.status = ProcessingStatus.PREDICTING

					except Exception as e:
						page.status = ProcessingStatus.ERROR


				# self._analyzed_pages.append(self._pending_pages.popleft())
			self._thread_lock.release()

			print("AnalyzerThread sleeping for 5 seconds")
			time.sleep(5)	
