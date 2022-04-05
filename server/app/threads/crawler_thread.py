import itertools
import threading
import time
from collections import deque
from typing import List

from analyzer.controllers.page_controller import PageController
from app.models.processing_status import ProcessingStatus
from app.threads.worker import Worker


class CrawlerThread(Worker):

	def __init__(self, thread_lock, pending_queue, analyzed_pages, platform_running):
		super().__init__(thread_lock, pending_queue, analyzed_pages, platform_running)
		self._page_controller = PageController()

	def run(self):
		print("---started analyzer thread---")
		while self._do_run:

			self._thread_lock.acquire()
			for page in self._pending_pages:
				if page.status == ProcessingStatus.PENDING and not page.crawl_success:
					print("Found one page to crawl---", page.src)
					try:
						page.status = ProcessingStatus.CRAWLING
						self._page_controller.crawl_details(page)
						self._page_controller.save_js_file(page)
						print("Done crawling", page.src)
						page.crawl_success = True
					except Exception as e:
						print("CrawlerThread error: ", e)
						page.status = ProcessingStatus.ERROR # Set it to error then let another thread dump to analyzed pages
						# raise
			self._thread_lock.release()
			print("CrawlerThread sleeping for 5 seconds")
			# print("self._pending_pages: ", self._pending_pages)
			time.sleep(5) 
