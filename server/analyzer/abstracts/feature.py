from abc import ABC, abstractmethod, abstractproperty
# from analyzer.datatypes.js_file import Jsfile
from typing import Callable

class Feature(ABC):

	@abstractproperty
	def name(self):
		pass

	@abstractproperty
	def index_no(self):
		pass

	@abstractproperty
	def var_type(self):
		pass

	@abstractmethod
	def extract(self, js_file):
		pass