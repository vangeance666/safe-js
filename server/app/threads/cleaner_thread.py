import itertools
import threading
import time
from collections import deque
from typing import List

from app.models.processing_status import ProcessingStatus
from app.threads.worker import Worker
from analyzer.controllers.results_controller import ResultsController
from config import DONE_PAGES_SAVE_PATH, PENDING_PAGES_SAVE_PATH

class CleanerThread(Worker):
	
	def __init__(self, thread_lock, pending_pages, done_pages, platform_running):
		super().__init__(thread_lock, pending_pages, done_pages, platform_running)
		self._results_controller = ResultsController()

	def run(self):

		while self._do_run:
			self._thread_lock.acquire()
			for i, page in enumerate(self._pending_pages):
				if page.status == ProcessingStatus.ERROR or page.status == ProcessingStatus.DONE:
					del self._pending_pages[i]
					self._done_pages.append(page)
					self._results_controller.save_pages(self._done_pages, DONE_PAGES_SAVE_PATH)
					self._results_controller.save_pages(self._pending_pages, PENDING_PAGES_SAVE_PATH)
					break
			self._thread_lock.release()

			print("CrawlerThread sleeping for 5 seconds")			

			print("pending_pages: ", len(self._pending_pages))
			print("done_pages: ", len(self._done_pages))
			time.sleep(5)
