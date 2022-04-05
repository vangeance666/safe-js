
from collections import deque
from typing import List

import threading
class Worker(threading.Thread):
	def __init__(self, thread_lock, pending_pages, done_pages, platform_running):
		super().__init__()
		self._thread_lock = thread_lock
		self._pending_pages: deque = pending_pages
		self._done_pages: List[Page] = done_pages
		self._do_run: bool = platform_running
	
	def run(self):
		raise NotImplementedError("Run not implemneted")