import itertools
import time
from collections import deque
from typing import List

# from analyzer.controllers.analysis_controller import AnalysisController
# from analyzer.controllers.features_controller import FeaturesController

from analyzer.controllers.inference_controller import InferenceController

from app.models.processing_status import ProcessingStatus
from app.threads.worker import Worker


class InferenceThread(Worker):
	
	def __init__(self, thread_lock, pending_pages, done_pages, platform_running):
		super().__init__(thread_lock, pending_pages, done_pages, platform_running)

		self._inference_controller = InferenceController()

	def run(self):
		print("---started analyzer thread---")
		while self._do_run:
			self._thread_lock.acquire()
			for page in self._pending_pages:
				if page.status == ProcessingStatus.ANALYZED \
					and page.is_analyzed \
					and page.features_extracted:
					print("Found one Page to predict js_files", page.src)
					try:
						page.status = ProcessingStatus.PREDICTING
						for js_file in itertools.chain(page.internal_js_files
							, page.external_js_files):

							print("InferenceThread Predicting ")
							self._inference_controller.predict(js_file)
						page.status = ProcessingStatus.DONE
					except Exception as e:
						page.error_reason = str(e)
						print("InferenceThread exception error: ", str(e))
						page.status = ProcessingStatus.ERROR
				# self._done_pages.append(self._pending_pages.popleft())
			self._thread_lock.release()

			print("InferenceThread sleeping for 5 seconds")
			time.sleep(5)	
