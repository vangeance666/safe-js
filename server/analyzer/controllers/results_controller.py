import pickle
from typing import List

from analyzer.datatypes.page import Page
from config import RESULTS_SAVED_PATH


class ResultsController:

	def __init__(self):
		self._data_path = RESULTS_SAVED_PATH

	def load_results(self):
		with open(self._data_path, 'rb') as f:
			return pickle.load(f)

	def save_results(self, pages: List[Page]):
		with open(self._data_path, 'wb') as f:
			pickle.dump(pages, fp)
