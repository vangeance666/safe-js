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
	def extract(self, js_file):
		pass


class DynamicFeature(Feature):
	pass


class IOCFeature(DynamicFeature):
	pass


class UrlsFeatures(DynamicFeature):
	pass


class ActiveUrlsFeature(DynamicFeature):
	pass

