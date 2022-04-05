
from collections import deque
from typing import List

import threading
class Worker(threading.Thread):
	def __init__(self, thread_lock, pending_queue, analyzed_pages, platform_running):
		super().__init__()
		self._thread_lock = thread_lock
		self._pending_pages: deque = pending_queue
		self._analyzed_pages: List[Page] = analyzed_pages
		self._do_run: bool = platform_running
	
	def run(self):
		raise NotImplementedError("Run not implemneted")