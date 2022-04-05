
import itertools
import threading
import time
from collections import deque
from typing import List

from app.threads.worker import Worker


class CleanerThread(Worker):
	
	def __init__(self, thread_lock, pending_queue, analyzed_pages, platform_running):
		super().__init__(thread_lock, pending_queue, analyzed_pages, platform_running)

	def run(self):

		while self._do_run:
			self._thread_lock.acquire()
			for i, page in enumerate(self._pending_pages):
				if page.status == "error" or page.status == "done":
					del self._pending_pages[i]
					self._analyzed_pages.append(page)
					break
			self._thread_lock.release()

			# print("CrawlerThread sleeping for 5 seconds")			
			time.sleep(5)