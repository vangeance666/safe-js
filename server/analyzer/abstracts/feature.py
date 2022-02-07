from abc import ABC, abstractmethod, abstractproperty


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
	def evaluate(self, js_buffer):
		pass

